# 📋 MÔ TẢ DỰ ÁN MVP (Frappe App: **miho\_cm** — Miho Construction Manager (mihocm))

*Cập nhật: 2025‑10‑03*

---

## 1) Định hướng chung

- **Tên app:** `mihocm` (Miho Construction Manager (mihocm))
- **Ngôn ngữ:** đa ngôn ngữ, ưu tiên **tiếng Việt trước** (VN-first).
- **Code convention:** tất cả biến, hàm, file, thư mục trong code sử dụng **tiếng Anh** để dễ maintain.
- **Triển khai:** SaaS đa tenant (site-per-tenant hoặc org-per-tenant).
- **Giao diện:** tối giản, role-based, phân biệt rõ người dùng văn phòng (PM/Owner) và công trường (Engineer/Supervisor/QC).
- **Triết lý UX:** “điền nhanh – duyệt nhanh – xem nhanh”, mobile-first cho công trường, dashboard rõ ràng cho PM/Owner.

---

## 2) Cấu trúc ứng dụng (dự kiến)

```
mihocm/
  ├── mihocm/
  │   ├── __init__.py
  │   ├── config/
  │   │   ├── desktop.py        # Workspace, module config
  │   │   ├── docs.py           # API docs config
  │   ├── modules.txt           # Danh sách module trong app
  │   ├── mihocm/
  │   │   ├── doctype/
  │   │   │   ├── project/
  │   │   │   ├── category/
  │   │   │   ├── task/
  │   │   │   ├── member/
  │   │   │   ├── daily_progress_log/
  │   │   │   ├── daily_resource_log/
  │   │   │   ├── daily_log_photo/
  │   │   └── report/
  │   ├── api/                  # REST endpoints cho mobile app/portal
  │   ├── services/             # Business logic (workflow, calculation)
  │   ├── utils/                # Helper functions
  │   ├── www/                  # Portal pages (Engineer portal, Share link)
  │   └── public/
  │       ├── css/
  │       ├── js/
  │       └── images/
  ├── patches.txt               # Migration patches
  └── README.md
```

---

## 3) DocType chi tiết

### 3.1 Project (Dự án)

- **Fields:**
  - `project_name` (Data, required)
  - `project_code` (Data, unique, optional)
  - `client_name` (Data)
  - `client_phone` (Data, optional, toggle hiển thị ở share link)
  - `address` (Small Text)
  - `location_map` (Data/URL, optional)
  - `scale` (Data)
  - `start_date` (Date)
  - `end_date` (Date)
  - `status` (Select: Draft/In Progress/Paused/Completed)
  - `cover_image` (Attach Image, required)
  - `description` (Text Editor)

### 3.2 Category (Hạng mục)

- **Fields:**
  - `project` (Link → Project, required)
  - `category_name` (Data, required)
  - `planned_start` (Date)
  - `planned_end` (Date)
  - `progress_weight` (Float, optional, % trọng số trong tiến độ dự án)
  - `notes` (Small Text)

### 3.3 Task (Đầu việc)

- **Fields:**
  - `project` (Link → Project, required)
  - `category` (Link → Category, required)
  - `task_name` (Data, required)
  - `unit` (Data/Select: m2, m3, tấn, bộ…)
  - `planned_quantity` (Float, optional)
  - `actual_quantity` (Float, auto-calculated from Daily Resource Logs)
  - `assignee` (Link → User, optional)
  - `notes` (Small Text)

### 3.4 Member (Thành viên dự án)

- **Fields:**
  - `project` (Link → Project, required)
  - `user` (Link → User, required)
  - `role` (Select: Owner/PM/Engineer/Supervisor/QC)
  - `active` (Check, default=1)

### 3.5 Daily Progress Log (Nhật ký tiến độ)

- **Mục đích:** báo cáo tiến độ, minh chứng cho khách hàng.
- **Fields:**
  - `project` (Link → Project, required)
  - `category` (Link → Category, required)
  - `task` (MultiSelect → Task)
  - `date` (Date, default=Today)
  - `shift` (Select: Morning/Afternoon/Night)
  - `description` (Text Editor, required)
  - `photos` (Table → Daily Log Photo, required ≥1)
  - `status` (Workflow: Draft → Pending Supervisor → Approved → Finalized by QC)
  - `qc_rating` (Select: Pass/Fail or 1–5)
  - `qc_comment` (Small Text)
- **Chia sẻ:** Yes (Client Portal) nhưng **ẩn toàn bộ số liệu khối lượng/chi phí**.

### 3.6 Daily Resource Log (Nhật ký nguồn lực nội bộ)

- **Mục đích:** quản lý nhân công, vật tư, máy móc, khối lượng để hạch toán nội bộ.
- **Fields:**
  - `project` (Link → Project, required)
  - `category` (Link → Category, required)
  - `task` (Link → Task, required)
  - `date` (Date, default=Today)
  - `labor_count` (Int)
  - `material_type` (Link → Item/Material)
  - `material_quantity` (Float)
  - `machine_type` (Link → Machine)
  - `machine_hours` (Float)
  - `actual_quantity` (Float)
  - `issues` (Table: Issue tags, optional — VD: thiếu vật tư, thời tiết xấu)
  - `weather` (Select: Nắng/Mưa/Khác)
  - `notes` (Small Text)
- **Chia sẻ:** No (nội bộ).
- **Liên kết Finance:** dùng dữ liệu này × đơn giá để tính chi phí.

### 3.7 Daily Log Photo (Ảnh nhật ký)

- **Fields:**
  - `daily_log` (Link → Daily Progress Log)
  - `image` (Attach Image, required)
  - `caption` (Small Text)

### 3.8 QC Checklist (tùy chọn mở rộng)

- Cho phép gắn checklist nghiệm thu vào Task hoặc Progress Log.
- Các item: đạt/chưa đạt, ghi chú.
- Lưu trong child table `qc_check_item`.

---

## 4) Workflow

### Daily Progress Log

1. **Engineer**: Draft → Submit → Pending Supervisor Review
2. **Supervisor**: Approve → Approved / Decline (có comment)
3. **QC**: Finalize (rating + comment) → Finalized\
   👉 Client Portal chỉ thấy mô tả + ảnh + QC status.

### Daily Resource Log

- Engineer/Đội trưởng nhập resource (labor, material, machine, actual\_quantity).
- Supervisor xác nhận.
- Dữ liệu chuyển sang Finance (nội bộ).\
  👉 Không chia sẻ ra ngoài.

### Project

- Draft → In Progress → Paused/Completed

---

## 5) Giao diện & UX

- **Owner/PM:** Dashboard đẹp, card dự án có ảnh cover, % tiến độ, QC rating.
- **Engineer (mobile-first):** form wizard → chọn Project → Hạng mục → Task → nhập mô tả/khối lượng → upload ảnh.
- **Supervisor:** Review Queue (Progress + Resource), approve/decline nhanh.
- **QC:** QC Inbox, finalize log, chấm rating, checklist.
- **Client Portal:** chỉ hiển thị Progress Log (ảnh + mô tả + QC), tiến độ %, không có khối lượng/chi phí.

👉 UX key: **PM/Owner cần tổng quan, kỹ sư cần nhập nhanh, khách hàng cần minh chứng dễ hiểu.**

---

## 6) Báo cáo

- **Tiến độ (Client-facing):** % hoàn thành theo hạng mục, ảnh, QC status, timeline.
- **Tài chính (Internal):** chi phí nhân công, vật tư, máy móc (Resource Logs), so sánh dự toán vs thực tế.
- **Resource Usage:** tổng hợp số công, vật tư, máy móc.
- **QC Report:** tổng hợp lỗi/sự cố, loại lỗi phổ biến.

---

## 7) Lưu trữ & Media

- MVP: dùng file storage mặc định Frappe.
- Option nâng cấp S3/MinIO.
- ≥1 ảnh/log; tự resize ảnh để nhẹ, phù hợp môi trường công trường.

---

## 8) Bảo mật & Quyền

- Cách ly dữ liệu theo tenant.
- Row-level filter theo Project.
- Audit trail bật cho cả Progress Log & Resource Log.
- Client chỉ thấy Progress Log.
- Branding: cho phép mỗi tenant gắn logo riêng (portal page).

---

📌 **Lưu ý:** Roadmap chi tiết (Phase 1–3 và mở rộng) sẽ viết trong file riêng `docs/ROADMAP_MVP.md`.

