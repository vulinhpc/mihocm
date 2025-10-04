# Frappe App Structure Guide - Chuẩn Thực Tế

## 🚨 **CẢNH BÁO QUAN TRỌNG**

Tài liệu chính thức của Frappe **KHÔNG ĐẦY ĐỦ** và có nhiều lỗi. Hướng dẫn này dựa trên kinh nghiệm thực tế và phân tích cấu trúc ERPNext.

## 📁 **CẤU TRÚC APP CHUẨN**

### **Cấu trúc thư mục đúng:**
```
your_app/
├── your_app/                    # Tên app (phải trùng với tên thư mục)
│   ├── __init__.py             # BẮT BUỘC: Có __version__
│   ├── hooks.py                # BẮT BUỘC: Cấu hình app
│   ├── modules.txt             # BẮT BUỘC: Danh sách modules
│   ├── patches.txt             # Tùy chọn: Patches
│   ├── doctype/                # BẮT BUỘC: Chứa DocTypes
│   │   ├── project/
│   │   │   ├── __init__.py
│   │   │   ├── project.json
│   │   │   └── project.py
│   │   └── ...
│   ├── modules/                # BẮT BUỘC: Chứa modules
│   │   ├── __init__.py
│   │   ├── project/
│   │   │   ├── __init__.py
│   │   │   └── project.py
│   │   └── ...
│   └── ...
├── pyproject.toml              # BẮT BUỘC: Cấu hình Python
├── README.md
└── docs/                       # Tài liệu
```

## ⚠️ **CÁC LỖI THƯỜNG GẶP**

### **1. Module và DocType trùng tên**
```bash
# ❌ SAI - Gây xung đột
your_app/
├── doctype/
│   └── project/
└── project/                    # ❌ Trùng tên với DocType

# ✅ ĐÚNG - Tách biệt rõ ràng
your_app/
├── doctype/
│   └── project/
└── modules/
    └── project/
```

### **2. Hooks.py thiếu cấu hình**
```python
# ❌ SAI - Thiếu nhiều trường bắt buộc
app_modules = ["project", "category"]

# ✅ ĐÚNG - Đầy đủ cấu hình
import os
from . import __version__ as app_version

app_name = "your_app"
app_title = "Your App Title"
app_publisher = "Your Name"
app_description = "Your app description"
app_email = "your@email.com"
app_license = "MIT"
app_logo_url = "/assets/your_app/images/logo.svg"
develop_version = "0.0.1-develop"

app_modules = [
    "project",
    "category",
    "task"
]

# Các trường bắt buộc khác
notification_config = "frappe.core.notifications.get_notification_config"
app_include_js = []
app_include_css = []
app_include_icons = []
doctype_js = {}
web_include_js = []
web_include_css = []
email_css = []
website_route_rules = []
website_redirects = []
base_template = "templates/base.html"
write_file_keys = []
before_tests = None
email_append_to = []
calendars = []
leaderboards = None
on_session_creation = []
on_login = None
on_logout = None
pdf_header_html = None
pdf_body_html = None
pdf_footer_html = None
permission_query_conditions = {}
scheduler_events = {}
fixtures = []
auto_update = False
update = None
before_install = None
after_install = None
before_uninstall = None
after_uninstall = None
```

### **3. Modules.txt sai format**
```bash
# ❌ SAI - Không có dòng trống cuối
Project
Category
Task

# ✅ ĐÚNG - Có dòng trống cuối
Project
Category
Task
```

## 🔧 **HƯỚNG DẪN TẠO APP CHUẨN**

### **Bước 1: Tạo app**
```bash
bench new-app your_app_name
```

### **Bước 2: Sửa cấu trúc thư mục**
```bash
cd apps/your_app_name/your_app_name
mkdir -p modules
mkdir -p doctype
```

### **Bước 3: Tạo modules**
```bash
# Tạo module cho mỗi DocType
mkdir -p modules/project
mkdir -p modules/category
mkdir -p modules/task

# Tạo file __init__.py
touch modules/__init__.py
touch modules/project/__init__.py
touch modules/category/__init__.py
touch modules/task/__init__.py

# Tạo file module
echo "# Project Module" > modules/project/project.py
echo "# Category Module" > modules/category/category.py
echo "# Task Module" > modules/task/task.py
```

### **Bước 4: Sửa hooks.py**
```python
import os
from . import __version__ as app_version

app_name = "your_app_name"
app_title = "Your App Title"
app_publisher = "Your Name"
app_description = "Your app description"
app_email = "your@email.com"
app_license = "MIT"
app_logo_url = "/assets/your_app_name/images/logo.svg"
develop_version = "0.0.1-develop"

app_modules = [
    "project",
    "category",
    "task"
]

# Các trường bắt buộc khác...
```

### **Bước 5: Sửa modules.txt**
```bash
Project
Category
Task
```

### **Bước 6: Tạo DocTypes**
```bash
# Tạo DocType project
mkdir -p doctype/project
touch doctype/project/__init__.py
# Tạo project.json và project.py
```

## 🧪 **KIỂM TRA APP**

### **1. Kiểm tra cấu trúc**
```bash
# Kiểm tra không có module trùng tên với DocType
ls -la your_app/
# Chỉ nên có: doctype/, modules/, hooks.py, modules.txt

# Kiểm tra modules/
ls -la your_app/modules/
# Nên có: __init__.py, project/, category/, task/

# Kiểm tra doctype/
ls -la your_app/doctype/
# Nên có: project/, category/, task/
```

### **2. Test migration**
```bash
bench --site your_site migrate
# Nếu thành công: DocTypes sẽ được tạo trong database
```

### **3. Kiểm tra DocTypes trong database**
```bash
bench --site your_site mariadb -e "SELECT name, module FROM tabDocType WHERE module = 'your_app_name';"
```

## 🚨 **TROUBLESHOOTING**

### **Lỗi: ModuleNotFoundError**
- **Nguyên nhân:** Module không tồn tại hoặc cấu trúc sai
- **Giải pháp:** Kiểm tra cấu trúc thư mục và file __init__.py

### **Lỗi: DocType không migrate**
- **Nguyên nhân:** Hooks.py thiếu cấu hình hoặc cấu trúc sai
- **Giải pháp:** Kiểm tra hooks.py và modules.txt

### **Lỗi: Module trùng tên**
- **Nguyên nhân:** Module và DocType cùng tên
- **Giải pháp:** Tách riêng vào thư mục modules/ và doctype/

## 📚 **TÀI LIỆU THAM KHẢO**

- [ERPNext GitHub](https://github.com/frappe/erpnext) - Cấu trúc app chuẩn
- [Frappe Framework](https://github.com/frappe/frappe) - Framework core
- [Frappe School](https://frappe.school/) - Học Frappe

## ⚡ **TIPS QUAN TRỌNG**

1. **Luôn tách riêng** modules và DocTypes
2. **Hooks.py phải đầy đủ** tất cả trường bắt buộc
3. **Test migration** sau mỗi thay đổi
4. **Tham khảo ERPNext** để hiểu cấu trúc chuẩn
5. **Không tin tài liệu chính thức** - test thực tế

---

**Lưu ý:** Tài liệu này được viết dựa trên kinh nghiệm thực tế và phân tích cấu trúc ERPNext. Tài liệu chính thức của Frappe có nhiều lỗi và không đầy đủ.
