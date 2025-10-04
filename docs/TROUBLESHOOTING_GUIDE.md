# Frappe App Troubleshooting Guide - Hướng Dẫn Sửa Lỗi

## 🚨 **CẢNH BÁO**

Tài liệu chính thức của Frappe **THIẾU HƯỚNG DẪN SỬA LỖI**. Hướng dẫn này dựa trên kinh nghiệm thực tế và các lỗi thường gặp.

## 🔍 **CÁC LỖI THƯỜNG GẶP VÀ CÁCH SỬA**

### **1. ModuleNotFoundError: No module named 'your_app'**

#### **Triệu chứng:**
```bash
ModuleNotFoundError: No module named 'mihocm'
```

#### **Nguyên nhân:**
- App không được cài đặt đúng cách
- Thiếu file `__init__.py` hoặc `__version__`
- Cấu trúc thư mục sai

#### **Cách sửa:**
```bash
# 1. Kiểm tra cấu trúc thư mục
ls -la apps/your_app/your_app/
# Phải có: __init__.py, hooks.py, modules.txt

# 2. Kiểm tra __init__.py có __version__
cat apps/your_app/your_app/__init__.py
# Phải có: __version__ = "0.0.1"

# 3. Cài đặt lại app
cd apps/your_app
pip install -e .

# 4. Restart bench
bench restart
```

### **2. ModuleNotFoundError: No module named 'your_app.module'**

#### **Triệu chứng:**
```bash
ModuleNotFoundError: No module named 'mihocm.project'
```

#### **Nguyên nhân:**
- Module không tồn tại trong thư mục `modules/`
- Thiếu file `__init__.py` trong module
- Cấu trúc thư mục sai

#### **Cách sửa:**
```bash
# 1. Tạo thư mục modules nếu chưa có
mkdir -p apps/your_app/your_app/modules

# 2. Tạo module
mkdir -p apps/your_app/your_app/modules/project
touch apps/your_app/your_app/modules/project/__init__.py
echo "# Project Module" > apps/your_app/your_app/modules/project/project.py

# 3. Cập nhật hooks.py
# Đảm bảo app_modules = ["project"] (không có prefix)

# 4. Restart bench
bench restart
```

### **3. DocType không migrate**

#### **Triệu chứng:**
```bash
# Migration chạy thành công nhưng DocType không xuất hiện trong database
bench --site your_site mariadb -e "SELECT name FROM tabDocType WHERE module = 'your_app';"
# Kết quả: (empty)
```

#### **Nguyên nhân:**
- Hooks.py thiếu cấu hình
- Modules.txt sai format
- Cấu trúc DocType sai

#### **Cách sửa:**
```bash
# 1. Kiểm tra hooks.py
cat apps/your_app/your_app/hooks.py
# Phải có: notification_config = "frappe.core.notifications.get_notification_config"

# 2. Kiểm tra modules.txt
cat apps/your_app/your_app/modules.txt
# Phải có: Project (tên module, không có prefix)

# 3. Kiểm tra cấu trúc DocType
ls -la apps/your_app/your_app/doctype/project/
# Phải có: __init__.py, project.json, project.py

# 4. Clear cache và migrate lại
bench --site your_site clear-cache
bench --site your_site migrate
```

### **4. AttributeError: 'NoneType' object has no attribute 'split'**

#### **Triệu chứng:**
```bash
AttributeError: 'NoneType' object has no attribute 'split'
```

#### **Nguyên nhân:**
- `notification_config = None` trong hooks.py
- Frappe không thể xử lý None value

#### **Cách sửa:**
```python
# ❌ SAI
notification_config = None

# ✅ ĐÚNG
notification_config = "frappe.core.notifications.get_notification_config"
```

### **5. Module và DocType trùng tên**

#### **Triệu chứng:**
```bash
# App có cấu trúc:
your_app/
├── doctype/
│   └── project/
└── project/  # ❌ Trùng tên với DocType
```

#### **Nguyên nhân:**
- Tạo module trùng tên với DocType
- Gây xung đột trong Frappe

#### **Cách sửa:**
```bash
# 1. Xóa module trùng tên
rm -rf apps/your_app/your_app/project/

# 2. Tạo module trong thư mục modules/
mkdir -p apps/your_app/your_app/modules/project
touch apps/your_app/your_app/modules/project/__init__.py
echo "# Project Module" > apps/your_app/your_app/modules/project/project.py

# 3. Cập nhật hooks.py
# app_modules = ["project"] (không có prefix)
```

### **6. Website lỗi 500 sau khi cài app**

#### **Triệu chứng:**
```bash
curl -Is http://localhost:8000
# HTTP/1.1 500 Internal Server Error
```

#### **Nguyên nhân:**
- App có lỗi cấu trúc
- Frappe không thể load app

#### **Cách sửa:**
```bash
# 1. Kiểm tra log
bench --site your_site console
# Tìm lỗi trong log

# 2. Tạm thời gỡ app
bench --site your_site uninstall-app your_app

# 3. Sửa lỗi app
# Kiểm tra hooks.py, modules.txt, cấu trúc thư mục

# 4. Cài lại app
bench --site your_site install-app your_app
```

### **7. DocType không hiển thị trong backend**

#### **Triệu chứng:**
- DocType không xuất hiện trong danh sách DocType
- Không thể tạo record mới

#### **Nguyên nhân:**
- DocType chưa được migrate
- Thiếu permissions
- Module không được load

#### **Cách sửa:**
```bash
# 1. Kiểm tra DocType trong database
bench --site your_site mariadb -e "SELECT name, module FROM tabDocType WHERE module = 'your_app';"

# 2. Nếu không có, migrate lại
bench --site your_site migrate

# 3. Kiểm tra permissions
bench --site your_site console
# frappe.get_doc("DocType", "Your DocType").permissions

# 4. Clear cache
bench --site your_site clear-cache
```

## 🔧 **CÔNG CỤ DEBUG**

### **1. Kiểm tra cấu trúc app**
```bash
# Kiểm tra cấu trúc tổng thể
tree apps/your_app/your_app/

# Kiểm tra modules
ls -la apps/your_app/your_app/modules/

# Kiểm tra doctypes
ls -la apps/your_app/your_app/doctype/
```

### **2. Kiểm tra cấu hình**
```bash
# Kiểm tra hooks.py
cat apps/your_app/your_app/hooks.py

# Kiểm tra modules.txt
cat apps/your_app/your_app/modules.txt

# Kiểm tra __init__.py
cat apps/your_app/your_app/__init__.py
```

### **3. Kiểm tra database**
```bash
# Kiểm tra DocTypes
bench --site your_site mariadb -e "SELECT name, module FROM tabDocType WHERE module = 'your_app';"

# Kiểm tra modules
bench --site your_site mariadb -e "SELECT name FROM tabModule Def WHERE app_name = 'your_app';"
```

### **4. Kiểm tra log**
```bash
# Kiểm tra log bench
tail -f logs/bench.log

# Kiểm tra log site
tail -f logs/your_site/error.log
```

## 📋 **CHECKLIST SỬA LỖI**

### **Trước khi báo lỗi:**
- [ ] Kiểm tra cấu trúc thư mục
- [ ] Kiểm tra hooks.py đầy đủ
- [ ] Kiểm tra modules.txt đúng format
- [ ] Kiểm tra __init__.py có __version__
- [ ] Kiểm tra không có module trùng tên với DocType
- [ ] Clear cache và restart bench
- [ ] Kiểm tra log lỗi

### **Khi tạo app mới:**
- [ ] Tạo cấu trúc thư mục đúng
- [ ] Sử dụng template hooks.py chuẩn
- [ ] Tạo modules trong thư mục modules/
- [ ] Tạo DocTypes trong thư mục doctype/
- [ ] Test migration sau mỗi thay đổi
- [ ] Kiểm tra DocTypes trong database

## 🚨 **LƯU Ý QUAN TRỌNG**

1. **Luôn backup** trước khi sửa lỗi
2. **Test migration** sau mỗi thay đổi
3. **Không tin tài liệu chính thức** - test thực tế
4. **Tham khảo ERPNext** để hiểu cấu trúc chuẩn
5. **Ghi lại các lỗi** để tránh lặp lại

## 📚 **TÀI LIỆU THAM KHẢO**

- [Frappe GitHub Issues](https://github.com/frappe/frappe/issues)
- [ERPNext GitHub Issues](https://github.com/frappe/erpnext/issues)
- [Frappe Forum](https://discuss.frappe.io/)

---

**Lưu ý:** Hướng dẫn này được viết dựa trên kinh nghiệm thực tế. Tài liệu chính thức của Frappe thiếu nhiều thông tin troubleshooting quan trọng.
