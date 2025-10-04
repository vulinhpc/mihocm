# Hướng dẫn cài đặt Miho Construction Management App

## 🎯 Mục tiêu
Hướng dẫn chi tiết cách cài đặt app mihocm vào Frappe site một cách chính xác.

## ⚠️ Lưu ý quan trọng
App này đã được fix để cài đặt thành công ngay từ lần đầu mà không cần fix thêm.

## 📋 Yêu cầu hệ thống

### Frappe Framework
- Frappe v14.0+ 
- ERPNext v14.0+ (tùy chọn)

### Hệ thống
- Python 3.8+
- MariaDB 10.3+
- Redis
- Node.js 14+

## 🚀 Cài đặt từng bước

### Bước 1: Chuẩn bị bench
```bash
# Tạo bench mới (nếu chưa có)
bench init [BENCH_NAME] --frappe-branch version-14

# Hoặc sử dụng bench hiện có
cd [BENCH_PATH]
```

### Bước 2: Cài đặt app
```bash
# Clone app từ GitHub
bench get-app https://github.com/vulinhpc/mihocm.git

# Kiểm tra app đã được cài đặt
bench list-apps
```

### Bước 3: Cài đặt vào site
```bash
# Tạo site mới (nếu chưa có)
bench new-site [SITE_NAME] --db-root-password [DB_PASSWORD]

# Cài đặt app vào site
bench --site [SITE_NAME] install-app mihocm

# Migration database
bench --site [SITE_NAME] migrate
```

### Bước 4: Khởi động server
```bash
# Khởi động server
bench start

# Hoặc chạy production
bench serve --port 8000
```

## 🔍 Kiểm tra cài đặt

### Kiểm tra app trong site
```bash
# Kiểm tra apps đã cài đặt
bench --site [SITE_NAME] list-apps

# Kiểm tra modules
bench --site [SITE_NAME] console
>>> frappe.get_list('Module Def', filters={'app_name': 'mihocm'})
```

### Kiểm tra DocTypes
```bash
# Kiểm tra DocTypes
bench --site [SITE_NAME] console
>>> frappe.get_list('DocType', filters={'module': 'mihocm'})
```

## 🌐 Truy cập website

### URL
```
http://localhost:8000
```

### Đăng nhập
- **Username**: Administrator
- **Password**: [PASSWORD_SETUP]

### Kiểm tra app
1. Vào **Apps** → **mihocm**
2. Kiểm tra các DocTypes: Project, Category, Task, Member, etc.

## 🛠️ Troubleshooting

### Lỗi thường gặp

#### 1. ModuleNotFoundError
```
ModuleNotFoundError: No module named 'mihocm'
```

**Nguyên nhân**: Cấu trúc module không đúng
**Giải pháp**: 
```bash
# Kiểm tra cấu trúc
ls -la apps/mihocm/mihocm/

# Phải có:
# - mihocm/ (module chính)
# - modules.txt
# - hooks.py
```

#### 2. Module trùng lặp
```
WARNING: module `mihocm` found in apps `frappe` and `mihocm`
```

**Nguyên nhân**: Module name bị trùng với Frappe core
**Giải pháp**: App đã được fix, không cần xử lý

#### 3. DocType không tìm thấy
```
DocType not found: Project
```

**Nguyên nhân**: DocTypes không nằm trong module đúng
**Giải pháp**:
```bash
# Kiểm tra DocTypes trong module
ls -la apps/mihocm/mihocm/mihocm/

# Phải có các thư mục: project, category, task, etc.
```

### Debug commands
```bash
# Kiểm tra logs
bench --site [SITE_NAME] console
>>> frappe.get_system_settings()

# Kiểm tra module map
>>> frappe.get_module_map()

# Kiểm tra hooks
>>> frappe.get_hooks()
```

## ✅ Checklist cài đặt

- [ ] Bench đã được tạo
- [ ] App mihocm đã được clone
- [ ] Site đã được tạo
- [ ] App đã được cài đặt vào site
- [ ] Migration đã chạy thành công
- [ ] Server đã khởi động
- [ ] Website có thể truy cập
- [ ] App mihocm hiển thị trong Apps
- [ ] Các DocTypes có thể tạo mới

## 📞 Hỗ trợ

Nếu gặp vấn đề trong quá trình cài đặt:

1. Kiểm tra logs: `bench --site [SITE_NAME] logs`
2. Kiểm tra cấu trúc app: `ls -la apps/mihocm/mihocm/`
3. Liên hệ: mrlinhvu1987@gmail.com

## 🔄 Cập nhật app

```bash
# Cập nhật app
bench update --patch

# Hoặc cập nhật app cụ thể
bench get-app https://github.com/vulinhpc/mihocm.git --force

# Migration sau khi cập nhật
bench --site [SITE_NAME] migrate
```
