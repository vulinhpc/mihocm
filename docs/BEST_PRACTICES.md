# Frappe App Best Practices - Thực Hành Tốt Nhất

## 🚨 **CẢNH BÁO**

Tài liệu chính thức của Frappe **THIẾU BEST PRACTICES**. Hướng dẫn này dựa trên phân tích ERPNext và kinh nghiệm thực tế.

## 🏗️ **CẤU TRÚC APP CHUẨN**

### **1. Tổ chức thư mục**
```
your_app/
├── your_app/                    # Tên app
│   ├── __init__.py             # BẮT BUỘC: Có __version__
│   ├── hooks.py                # BẮT BUỘC: Cấu hình đầy đủ
│   ├── modules.txt             # BẮT BUỘC: Danh sách modules
│   ├── patches.txt             # Tùy chọn: Patches
│   ├── doctype/                # BẮT BUỘC: DocTypes
│   │   ├── project/
│   │   │   ├── __init__.py
│   │   │   ├── project.json
│   │   │   └── project.py
│   │   └── ...
│   ├── modules/                # BẮT BUỘC: Modules
│   │   ├── __init__.py
│   │   ├── project/
│   │   │   ├── __init__.py
│   │   │   └── project.py
│   │   └── ...
│   ├── api/                    # Tùy chọn: API endpoints
│   ├── utils/                  # Tùy chọn: Utilities
│   ├── tests/                  # Tùy chọn: Tests
│   └── ...
├── pyproject.toml              # BẮT BUỘC: Cấu hình Python
├── README.md                   # Tùy chọn: Tài liệu
├── docs/                       # Tùy chọn: Tài liệu chi tiết
└── ...
```

### **2. Đặt tên chuẩn**
```python
# App name: snake_case
app_name = "construction_management"

# Module names: snake_case
app_modules = [
    "project_management",
    "resource_tracking",
    "daily_reports"
]

# DocType names: PascalCase
# Project Management
# Resource Tracking
# Daily Report
```

## 📝 **HOOKS.PY CHUẨN**

### **1. Cấu trúc hooks.py**
```python
import os
from . import __version__ as app_version

# ============================================================================
# APP INFORMATION
# ============================================================================
app_name = "your_app"
app_title = "Your App Title"
app_publisher = "Your Name"
app_description = "Your app description"
app_email = "your@email.com"
app_license = "MIT"
app_logo_url = "/assets/your_app/images/logo.svg"
develop_version = "0.0.1-develop"

# ============================================================================
# MODULES
# ============================================================================
app_modules = [
    "project",
    "category",
    "task"
]

# ============================================================================
# WEBSITE
# ============================================================================
app_include_js = []
app_include_css = []
app_include_icons = []

# ============================================================================
# DOCTYPE JS
# ============================================================================
doctype_js = {}

# ============================================================================
# WEBSITE JS/CSS
# ============================================================================
web_include_js = []
web_include_css = []

# ============================================================================
# EMAIL
# ============================================================================
email_css = []

# ============================================================================
# WEBSITE ROUTES
# ============================================================================
website_route_rules = []
website_redirects = []

# ============================================================================
# TEMPLATES
# ============================================================================
base_template = "templates/base.html"

# ============================================================================
# FILE HANDLING
# ============================================================================
write_file_keys = []

# ============================================================================
# NOTIFICATIONS
# ============================================================================
notification_config = "frappe.core.notifications.get_notification_config"

# ============================================================================
# TESTING
# ============================================================================
before_tests = None

# ============================================================================
# EMAIL APPEND
# ============================================================================
email_append_to = []

# ============================================================================
# CALENDARS
# ============================================================================
calendars = []

# ============================================================================
# LEADERBOARDS
# ============================================================================
leaderboards = None

# ============================================================================
# LOGIN/LOGOUT
# ============================================================================
on_session_creation = []
on_login = None
on_logout = None

# ============================================================================
# PDF
# ============================================================================
pdf_header_html = None
pdf_body_html = None
pdf_footer_html = None

# ============================================================================
# PERMISSIONS
# ============================================================================
permission_query_conditions = {}

# ============================================================================
# SCHEDULER
# ============================================================================
scheduler_events = {}

# ============================================================================
# FIXTURES
# ============================================================================
fixtures = []

# ============================================================================
# AUTO UPDATE
# ============================================================================
auto_update = False

# ============================================================================
# UPDATE
# ============================================================================
update = None

# ============================================================================
# INSTALL/UNINSTALL
# ============================================================================
before_install = None
after_install = None
before_uninstall = None
after_uninstall = None
```

### **2. Các trường bắt buộc**
```python
# LUÔN PHẢI CÓ
app_name = "your_app"
app_title = "Your App Title"
app_publisher = "Your Name"
app_description = "Your app description"
app_email = "your@email.com"
app_license = "MIT"
app_modules = ["project", "category"]
base_template = "templates/base.html"
notification_config = "frappe.core.notifications.get_notification_config"
```

## 📋 **MODULES.TXT CHUẨN**

### **1. Format chuẩn**
```bash
Project
Category
Task
Member
Daily Progress Log
Daily Resource Log
Daily Log Photo
```

### **2. Quy tắc đặt tên**
- **PascalCase** cho tên module
- **Một module per line**
- **Dòng trống cuối file**
- **Không có prefix app_name**

## 🗂️ **DOCTYPE CHUẨN**

### **1. Cấu trúc thư mục**
```
doctype/
├── project/
│   ├── __init__.py
│   ├── project.json
│   └── project.py
├── category/
│   ├── __init__.py
│   ├── category.json
│   └── category.py
└── ...
```

### **2. File project.json chuẩn**
```json
{
  "actions": [],
  "allow_rename": 1,
  "autoname": "field:project_name",
  "creation": "2025-10-04 09:00:00.000000",
  "default_view": "List",
  "doctype": "DocType",
  "editable_grid": 1,
  "engine": "InnoDB",
  "field_order": [
    "project_name",
    "column_break_2",
    "project_description"
  ],
  "fields": [
    {
      "fieldname": "project_name",
      "fieldtype": "Data",
      "in_list_view": 1,
      "label": "Project Name",
      "reqd": 1
    }
  ],
  "index_web_pages_for_search": 1,
  "links": [],
  "modified": "2025-10-04 09:00:00.000000",
  "modified_by": "Administrator",
  "module": "your_app",
  "name": "Project",
  "naming_rule": "By fieldname",
  "owner": "Administrator",
  "permissions": [
    {
      "create": 1,
      "delete": 1,
      "email": 1,
      "export": 1,
      "print": 1,
      "read": 1,
      "report": 1,
      "role": "System Manager",
      "share": 1,
      "write": 1
    }
  ],
  "sort_field": "modified",
  "sort_order": "DESC",
  "states": []
}
```

### **3. File project.py chuẩn**
```python
import frappe
from frappe.model.document import Document

class Project(Document):
    def validate(self):
        # Validation logic here
        pass
    
    def before_save(self):
        # Before save logic here
        pass
    
    def after_save(self):
        # After save logic here
        pass
```

## 🧪 **TESTING CHUẨN**

### **1. Cấu trúc test**
```
tests/
├── __init__.py
├── test_project.py
├── test_category.py
└── test_task.py
```

### **2. Test file chuẩn**
```python
import frappe
import unittest

class TestProject(unittest.TestCase):
    def setUp(self):
        self.project = frappe.get_doc({
            "doctype": "Project",
            "project_name": "Test Project"
        })
    
    def test_project_creation(self):
        self.project.insert()
        self.assertTrue(self.project.name)
    
    def tearDown(self):
        frappe.db.rollback()
```

## 📚 **DOCUMENTATION CHUẨN**

### **1. README.md**
```markdown
# Your App Name

## Description
Brief description of your app

## Installation
```bash
bench get-app https://github.com/your-username/your-app
bench --site your-site install-app your-app
```

## Usage
How to use your app

## Development
Development setup instructions

## License
MIT License
```

### **2. Docs structure**
```
docs/
├── README.md
├── INSTALLATION.md
├── USER_GUIDE.md
├── DEVELOPER_GUIDE.md
└── API_REFERENCE.md
```

## 🔧 **DEVELOPMENT WORKFLOW**

### **1. Tạo app mới**
```bash
# 1. Tạo app
bench new-app your_app_name

# 2. Sửa cấu trúc
cd apps/your_app_name/your_app_name
mkdir -p modules doctype

# 3. Sửa hooks.py theo template
# 4. Tạo modules và DocTypes
# 5. Test migration
bench --site your_site migrate
```

### **2. Phát triển DocType**
```bash
# 1. Tạo DocType
bench --site your_site console
# frappe.get_doc({"doctype": "DocType", "name": "Your DocType"}).insert()

# 2. Kiểm tra trong database
bench --site your_site mariadb -e "SELECT name FROM tabDocType WHERE module = 'your_app';"

# 3. Test functionality
# Tạo, sửa, xóa records
```

### **3. Deploy app**
```bash
# 1. Commit changes
git add .
git commit -m "Add new features"

# 2. Push to GitHub
git push origin main

# 3. Install on production
bench get-app https://github.com/your-username/your-app
bench --site production-site install-app your-app
```

## ⚠️ **CÁC LỖI THƯỜNG GẶP**

### **1. Module trùng tên với DocType**
```bash
# ❌ SAI
your_app/
├── doctype/project/
└── project/  # Trùng tên

# ✅ ĐÚNG
your_app/
├── doctype/project/
└── modules/project/
```

### **2. Hooks.py thiếu cấu hình**
```python
# ❌ SAI - Thiếu nhiều trường
app_modules = ["project"]

# ✅ ĐÚNG - Đầy đủ cấu hình
# Sử dụng template hooks.py chuẩn
```

### **3. Modules.txt sai format**
```bash
# ❌ SAI - Có prefix
mihocm.project
mihocm.category

# ✅ ĐÚNG - Không có prefix
Project
Category
```

## 🚀 **PERFORMANCE TIPS**

### **1. Tối ưu DocType**
- Sử dụng **index** cho các field thường query
- Tránh **Link** field không cần thiết
- Sử dụng **Table** thay vì **Child Table** khi có thể

### **2. Tối ưu hooks.py**
- Chỉ include **JS/CSS** cần thiết
- Sử dụng **lazy loading** cho modules
- Tránh **heavy operations** trong hooks

### **3. Tối ưu database**
- Sử dụng **select_into** cho bulk operations
- Tránh **N+1 queries**
- Sử dụng **caching** khi có thể

## 📚 **TÀI LIỆU THAM KHẢO**

- [ERPNext GitHub](https://github.com/frappe/erpnext) - App chuẩn
- [Frappe Framework](https://github.com/frappe/frappe) - Framework core
- [Frappe School](https://frappe.school/) - Học Frappe

---

**Lưu ý:** Best practices này được tổng hợp từ kinh nghiệm thực tế và phân tích ERPNext. Tài liệu chính thức của Frappe thiếu nhiều thông tin quan trọng.
