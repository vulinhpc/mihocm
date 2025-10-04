# Miho Construction Management App

## 📋 Mô tả
App quản lý dự án xây dựng được phát triển trên Frappe Framework.

## 🚀 Cài đặt

### Yêu cầu hệ thống
- Frappe Framework v14+
- Python 3.8+
- MariaDB 10.3+

### Cài đặt app
```bash
# Cài đặt app vào bench
bench get-app https://github.com/vulinhpc/mihocm.git

# Cài đặt app vào site
bench --site [SITE_NAME] install-app mihocm

# Migration database
bench --site [SITE_NAME] migrate
```

## 📁 Cấu trúc app

```
mihocm/
├── mihocm/                    # Module chính
│   ├── __init__.py
│   ├── project/               # DocType Project
│   ├── category/              # DocType Category
│   ├── task/                  # DocType Task
│   ├── member/                # DocType Member
│   ├── daily_progress_log/    # DocType Daily Progress Log
│   ├── daily_resource_log/    # DocType Daily Resource Log
│   └── daily_log_photo/       # DocType Daily Log Photo
├── hooks.py                   # Cấu hình app
├── modules.txt               # Danh sách modules
└── docs/                     # Documentation
```

## 🔧 Cấu hình

### File modules.txt
```
mihocm
project
category
task
member
daily_progress_log
daily_resource_log
daily_log_photo
```

### File hooks.py
```python
app_name = "mihocm"
app_title = "Miho Construction Managerment"
app_publisher = "Linh Vu"
app_description = "Miho construction managerment"
app_email = "mrlinhvu1987@gmail.com"
app_license = "mit"

app_modules = [
    "mihocm",
    "project",
    "category",
    "task",
    "member",
    "daily_progress_log",
    "daily_resource_log",
    "daily_log_photo"
]
```

## 📊 DocTypes

### 1. Project
- Quản lý thông tin dự án
- Fields: project_name, project_code, client_name, address, status, etc.

### 2. Category
- Phân loại dự án
- Fields: category_name, description

### 3. Task
- Quản lý công việc trong dự án
- Fields: task_name, project, assigned_to, status, etc.

### 4. Member
- Quản lý thành viên dự án
- Fields: member_name, role, contact_info

### 5. Daily Progress Log
- Ghi nhận tiến độ hàng ngày
- Fields: project, date, progress_notes, photos

### 6. Daily Resource Log
- Quản lý tài nguyên hàng ngày
- Fields: project, date, resources_used, quantity

### 7. Daily Log Photo
- Lưu trữ hình ảnh dự án
- Fields: project, date, photo, description

## 🛠️ Troubleshooting

### Lỗi ModuleNotFoundError
Nếu gặp lỗi `ModuleNotFoundError: No module named 'mihocm'`:

1. Kiểm tra file `modules.txt` có đúng format không
2. Kiểm tra file `__init__.py` trong module `mihocm`
3. Chạy migration: `bench --site [SITE_NAME] migrate`

### Lỗi module trùng lặp
Nếu gặp warning `module mihocm found in apps frappe and mihocm`:

1. Kiểm tra cấu trúc thư mục module
2. Đảm bảo DocTypes nằm trong module `mihocm`
3. Restart server: `bench restart`

## 📞 Hỗ trợ
- Email: mrlinhvu1987@gmail.com
- GitHub: https://github.com/vulinhpc/mihocm

## 📄 License
MIT License