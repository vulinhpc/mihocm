# 🏗️ Miho Construction Management (MihoCM)

## 📋 Mô Tả Dự Án

**MihoCM** là một ứng dụng quản lý dự án xây dựng được phát triển trên nền tảng Frappe Framework. Ứng dụng cung cấp các tính năng quản lý toàn diện cho các dự án xây dựng, từ lập kế hoạch đến theo dõi tiến độ và quản lý tài nguyên.

## 🎯 Tính Năng Chính

### **1. Quản Lý Dự Án (Project Management)**
- Tạo và quản lý các dự án xây dựng
- Theo dõi tiến độ tổng thể
- Quản lý thông tin dự án chi tiết

### **2. Phân Loại Công Việc (Category Management)**
- Tạo các danh mục công việc cho dự án
- Thiết lập trọng số tiến độ
- Quản lý thời gian dự kiến

### **3. Quản Lý Nhiệm Vụ (Task Management)**
- Tạo và phân công nhiệm vụ cụ thể
- Theo dõi số lượng kế hoạch vs thực tế
- Quản lý đơn vị đo lường (m2, m3, tấn, bộ, kg, litre, piece)

### **4. Quản Lý Thành Viên (Member Management)**
- Quản lý thành viên tham gia dự án
- Phân quyền theo vai trò (Owner, PM, Engineer, Supervisor, QC)
- Theo dõi trạng thái hoạt động

### **5. Ghi Nhận Tiến Độ (Daily Progress Log)**
- Ghi nhận tiến độ hàng ngày
- Cập nhật số lượng thực tế
- Ghi chú và báo cáo chi tiết

### **6. Quản Lý Tài Nguyên (Daily Resource Log)**
- Theo dõi nhân lực, thiết bị, vật liệu
- Ghi nhận số lượng sử dụng
- Quản lý đơn vị đo lường

### **7. Ghi Nhận Hình Ảnh (Daily Log Photo)**
- Lưu trữ hình ảnh tiến độ dự án
- Mô tả chi tiết từng hình ảnh
- Theo dõi tiến độ trực quan

## 🏗️ Cấu Trúc Ứng Dụng

```
mihocm/
├── mihocm/
│   ├── doctype/
│   │   ├── project/           # Quản lý dự án
│   │   ├── category/          # Phân loại công việc
│   │   ├── task/              # Quản lý nhiệm vụ
│   │   ├── member/            # Quản lý thành viên
│   │   ├── daily_progress_log/    # Ghi nhận tiến độ
│   │   ├── daily_resource_log/    # Quản lý tài nguyên
│   │   └── daily_log_photo/       # Ghi nhận hình ảnh
│   ├── hooks.py               # Cấu hình ứng dụng
│   └── modules.txt            # Danh sách modules
├── docs/                      # Tài liệu
├── README.md                  # Mô tả dự án
└── INSTALLATION.md            # Hướng dẫn cài đặt
```

## 🚀 Cài Đặt

Xem chi tiết hướng dẫn cài đặt tại [INSTALLATION.md](docs/INSTALLATION.md)

### **Cài đặt nhanh:**
```bash
# Cài app
bench get-app mihocm

# Cài vào site
bench --site [site_name] install-app mihocm

# Migrate
bench --site [site_name] migrate
```

## 📊 DocTypes

| DocType | Mô Tả | Trạng Thái |
|---------|-------|------------|
| **Project** | Quản lý dự án xây dựng | ✅ Hoàn thành |
| **Category** | Phân loại công việc | ✅ Hoàn thành |
| **Task** | Quản lý nhiệm vụ | ✅ Hoàn thành |
| **Member** | Quản lý thành viên | ✅ Hoàn thành |
| **Daily Progress Log** | Ghi nhận tiến độ | ✅ Hoàn thành |
| **Daily Resource Log** | Quản lý tài nguyên | ✅ Hoàn thành |
| **Daily Log Photo** | Ghi nhận hình ảnh | ✅ Hoàn thành |

## 🔧 Yêu Cầu Hệ Thống

- **Frappe Framework**: v14+
- **Python**: 3.8+
- **MariaDB**: 10.3+
- **Node.js**: 14+
- **Redis**: 6.0+

## 📝 License

MIT License - Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

## 👥 Tác Giả

**Linh Vu** - mrlinhvu1987@gmail.com

## 📞 Hỗ Trợ

Nếu gặp vấn đề trong quá trình sử dụng, vui lòng tạo issue trên GitHub hoặc liên hệ trực tiếp qua email.

---

**MihoCM** - Giải pháp quản lý dự án xây dựng toàn diện và hiệu quả! 🏗️✨