# Frappe hooks.py Template - Chuẩn Thực Tế

## 🚨 **CẢNH BÁO**

Tài liệu chính thức của Frappe về hooks.py **THIẾU NHIỀU TRƯỜNG BẮT BUỘC**. Template này dựa trên phân tích ERPNext và Frappe core.

## 📋 **TEMPLATE HOOKS.PY CHUẨN**

```python
import os

from . import __version__ as app_version

# ============================================================================
# APP INFORMATION - THÔNG TIN APP
# ============================================================================
app_name = "your_app_name"                    # Tên app (BẮT BUỘC)
app_title = "Your App Title"                  # Tiêu đề app (BẮT BUỘC)
app_publisher = "Your Name"                   # Tác giả (BẮT BUỘC)
app_description = "Your app description"      # Mô tả app (BẮT BUỘC)
app_email = "your@email.com"                 # Email liên hệ (BẮT BUỘC)
app_license = "MIT"                          # Giấy phép (BẮT BUỘC)
app_logo_url = "/assets/your_app/images/logo.svg"  # Logo URL (TÙY CHỌN)
develop_version = "0.0.1-develop"            # Phiên bản dev (TÙY CHỌN)

# ============================================================================
# MODULES - DANH SÁCH MODULES
# ============================================================================
app_modules = [
    "project",           # Module 1
    "category",          # Module 2
    "task",              # Module 3
    "member",            # Module 4
    # Thêm modules khác...
]

# ============================================================================
# WEBSITE - CẤU HÌNH WEBSITE
# ============================================================================
app_include_js = [
    # "your_app.bundle.js",  # JS bundle cho app
]

app_include_css = [
    # "your_app.bundle.css", # CSS bundle cho app
]

app_include_icons = [
    # "your_app/icons/icons.svg",  # Icons cho app
]

# ============================================================================
# DOCTYPE JAVASCRIPT - JS CHO DOCTYPE
# ============================================================================
doctype_js = {
    # "Your DocType": "public/js/your_app/your_doctype.js",
}

# ============================================================================
# WEBSITE JAVASCRIPT/CSS - JS/CSS CHO WEBSITE
# ============================================================================
web_include_js = [
    # "your_app/website_script.js",
]

web_include_css = [
    # "your_app/website.css",
]

# ============================================================================
# EMAIL - CẤU HÌNH EMAIL
# ============================================================================
email_css = [
    # "your_app/email.css",
]

# ============================================================================
# WEBSITE ROUTES - ĐỊNH TUYẾN WEBSITE
# ============================================================================
website_route_rules = [
    # {"from_route": "/your-route", "to_route": "Your DocType"},
]

website_redirects = [
    # {"source": "/old-route", "target": "/new-route"},
]

# ============================================================================
# TEMPLATES - TEMPLATE
# ============================================================================
base_template = "templates/base.html"        # Template cơ sở (BẮT BUỘC)

# ============================================================================
# FILE HANDLING - XỬ LÝ FILE
# ============================================================================
write_file_keys = [
    # "file_url", "file_name"  # Các key cho file
]

# ============================================================================
# NOTIFICATIONS - THÔNG BÁO
# ============================================================================
notification_config = "frappe.core.notifications.get_notification_config"  # BẮT BUỘC

# ============================================================================
# TESTING - KIỂM THỬ
# ============================================================================
before_tests = None  # "your_app.tests.before_tests"

# ============================================================================
# EMAIL APPEND - THÊM VÀO EMAIL
# ============================================================================
email_append_to = [
    # "Your DocType",  # DocTypes được thêm vào email
]

# ============================================================================
# CALENDARS - LỊCH
# ============================================================================
calendars = [
    # "Your DocType",  # DocTypes hiển thị trong lịch
]

# ============================================================================
# LEADERBOARDS - BẢNG XẾP HẠNG
# ============================================================================
leaderboards = None  # "your_app.leaderboard.get_leaderboards"

# ============================================================================
# LOGIN/LOGOUT - ĐĂNG NHẬP/ĐĂNG XUẤT
# ============================================================================
on_session_creation = [
    # "your_app.hooks.on_session_creation",
]

on_login = None  # "your_app.hooks.on_login"
on_logout = None  # "your_app.hooks.on_logout"

# ============================================================================
# PDF - CẤU HÌNH PDF
# ============================================================================
pdf_header_html = None  # "your_app.templates.pdf_header"
pdf_body_html = None    # "your_app.templates.pdf_body"
pdf_footer_html = None  # "your_app.templates.pdf_footer"

# ============================================================================
# PERMISSIONS - QUYỀN TRUY CẬP
# ============================================================================
permission_query_conditions = {
    # "Your DocType": "your_app.permissions.get_permission_query_conditions",
}

# ============================================================================
# SCHEDULER - LỊCH TRÌNH
# ============================================================================
scheduler_events = {
    # "daily": [
    #     "your_app.tasks.daily_task",
    # ],
    # "hourly": [
    #     "your_app.tasks.hourly_task",
    # ],
}

# ============================================================================
# FIXTURES - DỮ LIỆU MẪU
# ============================================================================
fixtures = [
    # {"dt": "Custom Field", "filters": [["name", "in", ["field1", "field2"]]]},
]

# ============================================================================
# AUTO UPDATE - TỰ ĐỘNG CẬP NHẬT
# ============================================================================
auto_update = False  # Tự động cập nhật

# ============================================================================
# UPDATE - CẬP NHẬT
# ============================================================================
update = None  # "your_app.patches.update"

# ============================================================================
# INSTALL/UNINSTALL - CÀI ĐẶT/GỠ BỎ
# ============================================================================
before_install = None  # "your_app.install.before_install"
after_install = None   # "your_app.install.after_install"
before_uninstall = None  # "your_app.install.before_uninstall"
after_uninstall = None   # "your_app.install.after_uninstall"
```

## 🔧 **HƯỚNG DẪN SỬ DỤNG**

### **1. Thay đổi thông tin app**
```python
app_name = "mihocm"                    # Tên app của bạn
app_title = "Miho Construction Management"  # Tiêu đề
app_publisher = "Linh Vu"              # Tác giả
app_description = "Construction management system"  # Mô tả
app_email = "mrlinhvu1987@gmail.com"   # Email
```

### **2. Thêm modules**
```python
app_modules = [
    "project",           # Module 1
    "category",          # Module 2
    "task",              # Module 3
    "member",            # Module 4
    "daily_progress_log", # Module 5
    "daily_resource_log", # Module 6
    "daily_log_photo",   # Module 7
]
```

### **3. Cấu hình website (nếu cần)**
```python
app_include_js = [
    "mihocm.bundle.js",  # JS bundle
]

app_include_css = [
    "mihocm.bundle.css", # CSS bundle
]
```

### **4. Cấu hình DocType JS (nếu cần)**
```python
doctype_js = {
    "Project": "public/js/mihocm/project.js",
    "Task": "public/js/mihocm/task.js",
}
```

## ⚠️ **CÁC TRƯỜNG BẮT BUỘC**

### **Luôn phải có:**
- `app_name`
- `app_title`
- `app_publisher`
- `app_description`
- `app_email`
- `app_license`
- `app_modules`
- `base_template`
- `notification_config`

### **Có thể để None:**
- `before_tests`
- `on_login`
- `on_logout`
- `pdf_header_html`
- `pdf_body_html`
- `pdf_footer_html`
- `leaderboards`
- `auto_update`
- `update`
- `before_install`
- `after_install`
- `before_uninstall`
- `after_uninstall`

## 🚨 **LỖI THƯỜNG GẶP**

### **1. Thiếu notification_config**
```python
# ❌ SAI - Gây lỗi migration
notification_config = None

# ✅ ĐÚNG
notification_config = "frappe.core.notifications.get_notification_config"
```

### **2. Thiếu base_template**
```python
# ❌ SAI - Gây lỗi
base_template = None

# ✅ ĐÚNG
base_template = "templates/base.html"
```

### **3. Thiếu import __version__**
```python
# ❌ SAI - Gây lỗi
app_name = "your_app"

# ✅ ĐÚNG
from . import __version__ as app_version
app_name = "your_app"
```

## 📚 **TÀI LIỆU THAM KHẢO**

- [Frappe hooks.py](https://github.com/frappe/frappe/blob/develop/frappe/hooks.py)
- [ERPNext hooks.py](https://github.com/frappe/erpnext/blob/develop/erpnext/hooks.py)

---

**Lưu ý:** Template này được tạo dựa trên phân tích cấu trúc thực tế của Frappe và ERPNext. Tài liệu chính thức thiếu nhiều thông tin quan trọng.
