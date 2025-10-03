# Hướng dẫn tạo Workspace trong Frappe

## Tổng quan
Workspace là nơi tổ chức các shortcuts và links trong Frappe Desk, giúp người dùng truy cập nhanh các tính năng quan trọng.

## Cách tạo Workspace cho Miho CM

### 1. Chuẩn bị cấu trúc JSON

Tạo file JSON với cấu trúc cơ bản:

```json
{
  "doctype": "Workspace",
  "name": "Miho CM",
  "title": "Miho CM", 
  "label": "Miho CM",
  "public": 1,
  "content": "[]",
  "parent_page": "",
  "module": "frappe",
  "is_default": 0,
  "developer_mode_only": 0
}
```

### 2. Thêm Shortcuts

Thêm các shortcuts hữu ích cho Construction Management:

```json
"shortcuts": [
  {
    "doctype": "Workspace Shortcut",
    "type": "DocType",
    "link_to": "Project",
    "title": "Projects",
    "label": "Projects",
    "icon": "folder",
    "color": "#FF6B6B"
  },
  {
    "doctype": "Workspace Shortcut",
    "type": "DocType",
    "link_to": "Task",
    "title": "Tasks",
    "label": "Tasks",
    "icon": "check",
    "color": "#4ECDC4"
  },
  {
    "doctype": "Workspace Shortcut",
    "type": "DocType",
    "link_to": "Customer",
    "title": "Customers",
    "label": "Customers",
    "icon": "users",
    "color": "#45B7D1"
  },
  {
    "doctype": "Workspace Shortcut",
    "type": "DocType",
    "link_to": "Employee",
    "title": "Employees",
    "label": "Employees",
    "icon": "user",
    "color": "#96CEB4"
  },
  {
    "doctype": "Workspace Shortcut",
    "type": "DocType",
    "link_to": "Item",
    "title": "Materials",
    "label": "Materials",
    "icon": "package",
    "color": "#FFEAA7"
  }
]
```

### 3. Import vào Database

Sử dụng lệnh bench để import:

```bash
cd /home/vulinhpc/miho-bench/frappe-bench
source env/bin/activate
bench --site mihocm.dev import-doc workspace_file.json
```

## Các lệnh quản lý Workspace

### Kiểm tra Workspace
```bash
bench --site mihocm.dev execute frappe.get_doc --args '["Workspace", "Miho CM"]'
```

### Xóa Workspace
```bash
bench --site mihocm.dev execute frappe.delete_doc --args '["Workspace", "Miho CM", 1]'
```

### Cập nhật Workspace
```bash
bench --site mihocm.dev import-doc updated_workspace.json
```

## Các loại Shortcuts

### 1. DocType Shortcut
```json
{
  "doctype": "Workspace Shortcut",
  "type": "DocType",
  "link_to": "Project",
  "title": "Projects",
  "label": "Projects",
  "icon": "folder",
  "color": "#FF6B6B"
}
```

### 2. Report Shortcut
```json
{
  "doctype": "Workspace Shortcut",
  "type": "Report",
  "link_to": "Project Profitability",
  "title": "Project Report",
  "label": "Project Report",
  "icon": "bar-chart",
  "color": "#4ECDC4"
}
```

### 3. Page Shortcut
```json
{
  "doctype": "Workspace Shortcut",
  "type": "Page",
  "link_to": "dashboard",
  "title": "Dashboard",
  "label": "Dashboard",
  "icon": "dashboard",
  "color": "#45B7D1"
}
```

### 4. URL Shortcut
```json
{
  "doctype": "Workspace Shortcut",
  "type": "URL",
  "link_to": "https://example.com",
  "title": "External Link",
  "label": "External Link",
  "icon": "external-link",
  "color": "#96CEB4"
}
```

## Các trường quan trọng

### Workspace Fields
- `name`: Tên duy nhất của workspace
- `title`: Tiêu đề hiển thị
- `label`: Nhãn hiển thị (bắt buộc)
- `public`: 1 = public, 0 = private
- `content`: JSON array chứa layout
- `module`: Module chứa workspace
- `is_default`: 1 = workspace mặc định
- `developer_mode_only`: 1 = chỉ hiện trong dev mode

### Shortcut Fields
- `type`: Loại shortcut (DocType, Report, Page, URL)
- `link_to`: Link đến đối tượng
- `title`: Tiêu đề hiển thị
- `label`: Nhãn hiển thị (bắt buộc)
- `icon`: Icon hiển thị
- `color`: Màu sắc

## Icons có sẵn

Frappe hỗ trợ các icons từ Font Awesome:
- `folder`, `file`, `users`, `user`
- `check`, `times`, `plus`, `minus`
- `bar-chart`, `pie-chart`, `line-chart`
- `dashboard`, `settings`, `cog`
- `external-link`, `download`, `upload`
- `package`, `truck`, `home`
- `calendar`, `clock`, `bell`

## Màu sắc

Sử dụng mã màu hex:
- `#FF6B6B` - Đỏ
- `#4ECDC4` - Xanh lá
- `#45B7D1` - Xanh dương
- `#96CEB4` - Xanh nhạt
- `#FFEAA7` - Vàng
- `#DDA0DD` - Tím
- `#98D8C8` - Xanh mint

## Troubleshooting

### Lỗi "Content data should be a list"
- Đảm bảo field `content` là `"[]"`

### Lỗi "Module not found"
- Sử dụng `"frappe"` thay vì custom module

### Lỗi "label is mandatory"
- Thêm field `label` cho tất cả shortcuts

### Workspace không hiển thị
- Kiểm tra `public = 1`
- Kiểm tra user có quyền truy cập
- Restart server nếu cần

## Ví dụ hoàn chỉnh

File `miho_cm_workspace.json`:

```json
{
  "doctype": "Workspace",
  "name": "Miho CM",
  "title": "Miho CM",
  "label": "Miho CM",
  "public": 1,
  "content": "[]",
  "parent_page": "",
  "module": "frappe",
  "is_default": 0,
  "developer_mode_only": 0,
  "shortcuts": [
    {
      "doctype": "Workspace Shortcut",
      "type": "DocType",
      "link_to": "Project",
      "title": "Projects",
      "label": "Projects",
      "icon": "folder",
      "color": "#FF6B6B"
    },
    {
      "doctype": "Workspace Shortcut",
      "type": "DocType",
      "link_to": "Task",
      "title": "Tasks",
      "label": "Tasks",
      "icon": "check",
      "color": "#4ECDC4"
    },
    {
      "doctype": "Workspace Shortcut",
      "type": "DocType",
      "link_to": "Customer",
      "title": "Customers",
      "label": "Customers",
      "icon": "users",
      "color": "#45B7D1"
    },
    {
      "doctype": "Workspace Shortcut",
      "type": "DocType",
      "link_to": "Employee",
      "title": "Employees",
      "label": "Employees",
      "icon": "user",
      "color": "#96CEB4"
    },
    {
      "doctype": "Workspace Shortcut",
      "type": "DocType",
      "link_to": "Item",
      "title": "Materials",
      "label": "Materials",
      "icon": "package",
      "color": "#FFEAA7"
    }
  ]
}
```

## Kết luận

Workspace giúp tổ chức và truy cập nhanh các tính năng quan trọng trong Frappe. Với hướng dẫn này, bạn có thể tạo workspace tùy chỉnh cho ứng dụng Miho CM.
