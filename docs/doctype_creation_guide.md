# Hướng dẫn tạo DocType trong Frappe

## 🎯 Mục tiêu
Hướng dẫn chi tiết cách tạo DocType trong Frappe Framework, dựa trên kinh nghiệm thực tế từ việc tạo DocType Project cho ứng dụng Miho Construction Management.

## 📝 Quy trình tạo DocType

### Phương pháp 1: Sử dụng Bench Console (Khuyến nghị)

Đây là phương pháp hiệu quả và đáng tin cậy nhất để tạo DocType.

#### Bước 1: Chuẩn bị môi trường
```bash
cd /path/to/your/frappe-bench
source env/bin/activate
```

#### Bước 2: Mở Frappe Console
```bash
bench --site your-site-name console
```

#### Bước 3: Tạo DocType cơ bản
```python
import frappe

# Tạo DocType cơ bản trước
doctype = frappe.get_doc({
    'doctype': 'DocType',
    'name': 'YourDocTypeName',
    'module': 'your_app_name',
    'fields': [
        {
            'fieldname': 'field_name',
            'fieldtype': 'Data',
            'label': 'Field Label',
            'reqd': 1  # Required field
        }
    ]
})

# Bỏ qua validation để tránh lỗi module
doctype.insert(ignore_links=True)
frappe.db.commit()
print('✅ DocType cơ bản đã được tạo!')
```

#### Bước 4: Thêm các fields chi tiết
```python
# Lấy DocType vừa tạo
doctype = frappe.get_doc('DocType', 'YourDocTypeName')

# Thêm các fields
doctype.append('fields', {
    'fieldname': 'field_name_2',
    'fieldtype': 'Data',
    'label': 'Field Label 2',
    'in_list_view': 1
})

# Cấu hình DocType properties
doctype.autoname = 'field:field_name'
doctype.default_view = 'List'
doctype.editable_grid = 1
doctype.track_changes = 1

# Lưu lại
doctype.save()
frappe.db.commit()
print('✅ Đã cấu hình đầy đủ DocType!')
```

#### Bước 5: Test DocType
```python
# Test tạo record mới
test_record = frappe.get_doc({
    'doctype': 'YourDocTypeName',
    'field_name': 'Test Value',
    'field_name_2': 'Test Value 2'
})

test_record.insert()
frappe.db.commit()
print('✅ Test tạo record thành công!')

# Xóa record test
frappe.delete_doc('YourDocTypeName', test_record.name)
frappe.db.commit()
print('🗑️ Đã xóa record test')
```

### Phương pháp 2: Tạo file JSON và Python (Truyền thống)

#### Bước 1: Tạo cấu trúc thư mục
```bash
mkdir -p apps/your_app/your_app/doctype/your_doctype
```

#### Bước 2: Tạo file JSON
Tạo file `apps/your_app/your_app/doctype/your_doctype/your_doctype.json`:

```json
{
    "doctype": "DocType",
    "name": "YourDocTypeName",
    "module": "your_app_name",
    "fields": [
        {
            "fieldname": "field_name",
            "fieldtype": "Data",
            "label": "Field Label",
            "reqd": 1,
            "in_list_view": 1
        }
    ],
    "permissions": [
        {
            "role": "System Manager",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1,
            "export": 1,
            "print": 1,
            "email": 1,
            "report": 1,
            "share": 1
        }
    ],
    "naming_rule": "By fieldname",
    "autoname": "field:field_name",
    "default_view": "List",
    "editable_grid": 1,
    "track_changes": 1
}
```

#### Bước 3: Tạo file Python
Tạo file `apps/your_app/your_app/doctype/your_doctype/your_doctype.py`:

```python
import frappe
from frappe.model.document import Document

class YourDocTypeName(Document):
    pass
```

#### Bước 4: Tạo file __init__.py
Tạo file `apps/your_app/your_app/doctype/your_doctype/__init__.py`:

```python
# Empty file
```

#### Bước 5: Chạy migration
```bash
bench --site your-site-name migrate
```

## 🔧 Các loại Field phổ biến

### 1. Data Fields
```python
{
    'fieldname': 'field_name',
    'fieldtype': 'Data',
    'label': 'Field Label',
    'reqd': 1,  # Required
    'unique': 1,  # Unique
    'in_list_view': 1  # Show in list view
}
```

### 2. Select Fields
```python
{
    'fieldname': 'status',
    'fieldtype': 'Select',
    'label': 'Status',
    'options': 'Draft\nIn Progress\nCompleted',
    'reqd': 1,
    'in_list_view': 1
}
```

### 3. Date Fields
```python
{
    'fieldname': 'start_date',
    'fieldtype': 'Date',
    'label': 'Start Date'
}
```

### 4. Check Fields
```python
{
    'fieldname': 'is_active',
    'fieldtype': 'Check',
    'label': 'Is Active'
}
```

### 5. Text Fields
```python
{
    'fieldname': 'description',
    'fieldtype': 'Small Text',  # hoặc 'Text Editor'
    'label': 'Description'
}
```

### 6. Attach Fields
```python
{
    'fieldname': 'attachment',
    'fieldtype': 'Attach',
    'label': 'Attachment'
}
```

### 7. Attach Image Fields
```python
{
    'fieldname': 'image',
    'fieldtype': 'Attach Image',
    'label': 'Image',
    'reqd': 1
}
```

## ⚠️ Lưu ý quan trọng

### 1. Module Validation
- Khi tạo DocType, Frappe sẽ validate module
- Nếu module chưa tồn tại, sử dụng `ignore_links=True` trong `insert()`
- Hoặc tạo DocType với module `frappe` trước, sau đó chuyển về module của app

### 2. Field Naming
- Sử dụng snake_case cho fieldname
- Tránh sử dụng từ khóa Python
- Đặt tên có ý nghĩa và dễ hiểu

### 3. Permissions
- Luôn cấu hình permissions cho DocType
- Mặc định cấp quyền cho System Manager
- Có thể thêm permissions cho các role khác

### 4. Testing
- Luôn test DocType sau khi tạo
- Test tạo, sửa, xóa records
- Kiểm tra validation rules

## 🚀 Ví dụ hoàn chỉnh: Tạo DocType Project

```python
import frappe

# Bước 1: Tạo DocType cơ bản
doctype = frappe.get_doc({
    'doctype': 'DocType',
    'name': 'Project',
    'module': 'mihocm',
    'fields': [
        {
            'fieldname': 'project_name',
            'fieldtype': 'Data',
            'label': 'Project Name',
            'reqd': 1,
            'in_list_view': 1
        }
    ]
})

doctype.insert(ignore_links=True)
frappe.db.commit()

# Bước 2: Thêm các fields chi tiết
doctype = frappe.get_doc('DocType', 'Project')

# Thêm fields
fields_to_add = [
    {
        'fieldname': 'project_code',
        'fieldtype': 'Data',
        'label': 'Project Code',
        'unique': 1,
        'in_list_view': 1
    },
    {
        'fieldname': 'client_name',
        'fieldtype': 'Data',
        'label': 'Client Name',
        'in_list_view': 1
    },
    {
        'fieldname': 'status',
        'fieldtype': 'Select',
        'label': 'Status',
        'options': 'Draft\nIn Progress\nPaused\nCompleted',
        'reqd': 1,
        'in_list_view': 1
    },
    {
        'fieldname': 'start_date',
        'fieldtype': 'Date',
        'label': 'Start Date'
    },
    {
        'fieldname': 'end_date',
        'fieldtype': 'Date',
        'label': 'End Date'
    },
    {
        'fieldname': 'description',
        'fieldtype': 'Text Editor',
        'label': 'Description'
    }
]

for field in fields_to_add:
    doctype.append('fields', field)

# Cấu hình DocType
doctype.autoname = 'field:project_code'
doctype.default_view = 'List'
doctype.editable_grid = 1
doctype.track_changes = 1

# Lưu lại
doctype.save()
frappe.db.commit()

print('✅ DocType Project đã được tạo thành công!')
```

## 🔍 Troubleshooting

### Lỗi "Could not find Module"
```python
# Giải pháp: Sử dụng ignore_links=True
doctype.insert(ignore_links=True)
```

### Lỗi "DocType already exists"
```python
# Giải pháp: Kiểm tra trước khi tạo
if not frappe.db.exists('DocType', 'YourDocTypeName'):
    # Tạo DocType
    pass
```

### Lỗi "Field validation failed"
```python
# Giải pháp: Kiểm tra field options
# Đảm bảo options cho Select field đúng format
'options': 'Option1\nOption2\nOption3'
```

## 📚 Tài liệu tham khảo

- [Frappe DocType Documentation](https://frappeframework.com/docs/user/en/doctype)
- [Frappe Field Types](https://frappeframework.com/docs/user/en/doctype#field-types)
- [Frappe Console Commands](https://frappeframework.com/docs/user/en/bench)

---

*Cập nhật: 2025-01-03*
*Dựa trên kinh nghiệm thực tế từ việc tạo DocType Project cho Miho Construction Management*
