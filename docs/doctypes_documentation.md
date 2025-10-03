# 📋 Tài liệu DocTypes - Miho Construction Management

*Cập nhật: 2025-10-03*

## 🎯 Tổng quan

Tài liệu này mô tả chi tiết tất cả các DocTypes đã được tạo cho ứng dụng Miho Construction Management (mihocm), bao gồm cấu trúc dữ liệu, mối quan hệ và mục đích sử dụng.

## 📊 Danh sách DocTypes

### Main DocTypes (6 DocTypes)

| DocType | Mô tả | Fields | Mục đích |
|---------|-------|--------|----------|
| **Project** | Dự án xây dựng | 13 fields | Quản lý thông tin dự án chính |
| **Category** | Hạng mục công việc | 6 fields | Phân chia dự án thành các hạng mục |
| **Task** | Đầu việc cụ thể | 8 fields | Quản lý các công việc chi tiết |
| **Member** | Thành viên dự án | 4 fields | Quản lý nhân sự và vai trò |
| **Daily Progress Log** | Nhật ký tiến độ | 10 fields | Báo cáo tiến độ cho khách hàng |
| **Daily Resource Log** | Nhật ký nguồn lực | 13 fields | Quản lý nguồn lực nội bộ |

### Child DocTypes (3 DocTypes)

| DocType | Mô tả | Fields | Mục đích |
|---------|-------|--------|----------|
| **Daily Log Photo** | Ảnh nhật ký | 3 fields | Lưu trữ ảnh minh chứng |
| **Daily Progress Log Task** | Task trong nhật ký | 1 field | Liên kết nhiều tasks |
| **Daily Resource Log Issue** | Vấn đề phát sinh | 1 field | Ghi nhận các vấn đề |

---

## 📋 Chi tiết từng DocType

### 1. Project (Dự án)

**Mục đích**: Quản lý thông tin chính của dự án xây dựng

**Fields**:
- `project_name` (Data, required): Tên dự án
- `project_code` (Data, unique): Mã dự án
- `client_name` (Data): Tên khách hàng
- `client_phone` (Data): Số điện thoại khách hàng
- `show_client_phone` (Check): Hiển thị số điện thoại ở share link
- `address` (Small Text): Địa chỉ dự án
- `location_map` (Data): Link bản đồ vị trí
- `scale` (Data): Quy mô dự án
- `start_date` (Date): Ngày bắt đầu
- `end_date` (Date): Ngày kết thúc
- `status` (Select): Trạng thái (Draft/In Progress/Paused/Completed)
- `cover_image` (Attach Image, required): Ảnh bìa dự án
- `description` (Text Editor): Mô tả chi tiết

**Mối quan hệ**:
- 1:N với Category
- 1:N với Member
- 1:N với Daily Progress Log
- 1:N với Daily Resource Log

### 2. Category (Hạng mục)

**Mục đích**: Phân chia dự án thành các hạng mục công việc

**Fields**:
- `project` (Link → Project, required): Dự án
- `category_name` (Data, required): Tên hạng mục
- `planned_start` (Date): Ngày bắt đầu dự kiến
- `planned_end` (Date): Ngày kết thúc dự kiến
- `progress_weight` (Float): Trọng số tiến độ (%)
- `notes` (Small Text): Ghi chú

**Mối quan hệ**:
- N:1 với Project
- 1:N với Task
- 1:N với Daily Progress Log
- 1:N với Daily Resource Log

### 3. Task (Đầu việc)

**Mục đích**: Quản lý các đầu việc cụ thể trong hạng mục

**Fields**:
- `project` (Link → Project, required): Dự án
- `category` (Link → Category, required): Hạng mục
- `task_name` (Data, required): Tên đầu việc
- `unit` (Select): Đơn vị (m2, m3, tấn, bộ, kg, litre, piece)
- `planned_quantity` (Float): Khối lượng dự kiến
- `actual_quantity` (Float, read-only): Khối lượng thực tế (tự động tính)
- `assignee` (Link → User): Người thực hiện
- `notes` (Small Text): Ghi chú

**Mối quan hệ**:
- N:1 với Project
- N:1 với Category
- 1:N với Daily Progress Log Task
- 1:N với Daily Resource Log

### 4. Member (Thành viên dự án)

**Mục đích**: Quản lý thành viên và vai trò trong dự án

**Fields**:
- `project` (Link → Project, required): Dự án
- `user` (Link → User, required): Người dùng
- `role` (Select, required): Vai trò (Owner/PM/Engineer/Supervisor/QC)
- `active` (Check, default=1): Trạng thái hoạt động

**Mối quan hệ**:
- N:1 với Project
- N:1 với User

### 5. Daily Progress Log (Nhật ký tiến độ)

**Mục đích**: Báo cáo tiến độ hàng ngày cho khách hàng

**Fields**:
- `project` (Link → Project, required): Dự án
- `category` (Link → Category, required): Hạng mục
- `task` (Table → Daily Progress Log Task, required): Danh sách tasks
- `date` (Date, default=Today, required): Ngày báo cáo
- `shift` (Select): Ca làm việc (Morning/Afternoon/Night)
- `description` (Text Editor, required): Mô tả công việc
- `photos` (Table → Daily Log Photo, required): Ảnh minh chứng
- `status` (Select, required): Trạng thái (Draft/Pending Supervisor/Approved/Finalized by QC)
- `qc_rating` (Select): Đánh giá QC (Pass/Fail/1/2/3/4/5)
- `qc_comment` (Small Text): Nhận xét QC

**Workflow**: Draft → Pending Supervisor → Approved → Finalized by QC

**Mối quan hệ**:
- N:1 với Project
- N:1 với Category
- 1:N với Daily Progress Log Task
- 1:N với Daily Log Photo

### 6. Daily Resource Log (Nhật ký nguồn lực)

**Mục đích**: Quản lý nhân công, vật tư, máy móc nội bộ

**Fields**:
- `project` (Link → Project, required): Dự án
- `category` (Link → Category, required): Hạng mục
- `task` (Link → Task, required): Đầu việc
- `date` (Date, default=Today, required): Ngày báo cáo
- `labor_count` (Int): Số lượng nhân công
- `material_type` (Data): Loại vật tư
- `material_quantity` (Float): Khối lượng vật tư
- `machine_type` (Data): Loại máy móc
- `machine_hours` (Float): Số giờ máy
- `actual_quantity` (Float): Khối lượng thực tế
- `issues` (Table → Daily Resource Log Issue): Danh sách vấn đề
- `weather` (Select): Thời tiết (Nắng/Mưa/Khác)
- `notes` (Small Text): Ghi chú

**Mối quan hệ**:
- N:1 với Project
- N:1 với Category
- N:1 với Task
- 1:N với Daily Resource Log Issue

### 7. Daily Log Photo (Ảnh nhật ký) - Child DocType

**Mục đích**: Lưu trữ ảnh minh chứng cho nhật ký tiến độ

**Fields**:
- `daily_log` (Link → Daily Progress Log, required): Nhật ký tiến độ
- `image` (Attach Image, required): Ảnh
- `caption` (Small Text): Chú thích ảnh

**Mối quan hệ**:
- N:1 với Daily Progress Log

### 8. Daily Progress Log Task (Task trong nhật ký) - Child DocType

**Mục đích**: Liên kết nhiều tasks với một nhật ký tiến độ

**Fields**:
- `task` (Link → Task, required): Đầu việc

**Mối quan hệ**:
- N:1 với Daily Progress Log
- N:1 với Task

### 9. Daily Resource Log Issue (Vấn đề phát sinh) - Child DocType

**Mục đích**: Ghi nhận các vấn đề phát sinh trong quá trình thi công

**Fields**:
- `issue_tag` (Data, required): Tag vấn đề

**Mối quan hệ**:
- N:1 với Daily Resource Log

---

## 🔗 Sơ đồ mối quan hệ

```
Project (1) ──→ (N) Category
Project (1) ──→ (N) Member
Project (1) ──→ (N) Daily Progress Log
Project (1) ──→ (N) Daily Resource Log

Category (1) ──→ (N) Task
Category (1) ──→ (N) Daily Progress Log
Category (1) ──→ (N) Daily Resource Log

Task (1) ──→ (N) Daily Progress Log Task
Task (1) ──→ (N) Daily Resource Log

Daily Progress Log (1) ──→ (N) Daily Progress Log Task
Daily Progress Log (1) ──→ (N) Daily Log Photo

Daily Resource Log (1) ──→ (N) Daily Resource Log Issue
```

---

## 🚀 Cách sử dụng

### 1. Tạo dự án mới
1. Tạo Project với thông tin cơ bản
2. Thêm Category cho các hạng mục chính
3. Tạo Task cho từng đầu việc cụ thể
4. Thêm Member với vai trò phù hợp

### 2. Báo cáo tiến độ hàng ngày
1. Tạo Daily Progress Log
2. Chọn Category và Tasks liên quan
3. Thêm mô tả và ảnh minh chứng
4. Gửi cho Supervisor để duyệt

### 3. Quản lý nguồn lực nội bộ
1. Tạo Daily Resource Log
2. Ghi nhận nhân công, vật tư, máy móc
3. Ghi chú các vấn đề phát sinh
4. Theo dõi khối lượng thực tế

---

## 📝 Ghi chú kỹ thuật

- **Module**: Tất cả DocTypes thuộc module `mihocm`
- **App**: Thuộc về app `mihocm`
- **Database**: Đã được migrate thành công
- **Files**: Tất cả files đã được tạo trong `apps/mihocm/mihocm/doctype/`
- **Permissions**: Mặc định cho System Manager

---

## 🔄 Cập nhật tiếp theo

- [ ] Tạo sample data
- [ ] Phát triển giao diện người dùng
- [ ] Tích hợp mobile app
- [ ] Tạo reports và dashboards
- [ ] Implement workflow automation

---

*Tài liệu này được tạo tự động từ cấu trúc DocTypes thực tế trong database.*
