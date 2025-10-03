# Miho Construction Management

Miho Construction Management (Miho CM) là ứng dụng quản lý xây dựng được phát triển trên nền tảng Frappe Framework, cung cấp các tính năng quản lý dự án, nhân viên, khách hàng và vật liệu xây dựng.

## 🎯 Tính năng chính

- 📁 **Quản lý dự án**: Theo dõi tiến độ và chi phí dự án
- ✅ **Quản lý công việc**: Phân công và theo dõi tasks theo hạng mục
- 👥 **Quản lý thành viên**: Phân quyền theo vai trò (Owner/PM/Engineer/Supervisor/QC)
- 📝 **Nhật ký tiến độ**: Báo cáo tiến độ cho khách hàng với workflow approval
- 📈 **Nhật ký nguồn lực**: Quản lý nhân công, vật tư, máy móc nội bộ
- 📸 **Minh chứng**: Lưu trữ ảnh và tài liệu minh chứng
- 🏗️ **Workspace tùy chỉnh**: Giao diện được tối ưu cho ngành xây dựng

## 📋 DocTypes đã tạo

### Main DocTypes (6)
- **Project**: Quản lý thông tin dự án chính
- **Category**: Phân chia dự án thành hạng mục
- **Task**: Quản lý các đầu việc cụ thể
- **Member**: Quản lý thành viên và vai trò
- **Daily Progress Log**: Báo cáo tiến độ cho khách hàng
- **Daily Resource Log**: Quản lý nguồn lực nội bộ

### Child DocTypes (3)
- **Daily Log Photo**: Lưu trữ ảnh minh chứng
- **Daily Progress Log Task**: Liên kết tasks với nhật ký
- **Daily Resource Log Issue**: Ghi nhận vấn đề phát sinh

## 🚀 Cài đặt

### Yêu cầu hệ thống
- Python 3.8+
- Node.js 14+
- MariaDB 10.3+
- Redis 6.0+
- Frappe Framework 15+

### Cài đặt nhanh

```bash
# Tạo site mới
bench new-site mihocm.dev

# Cài đặt app
bench --site mihocm.dev install-app mihocm

# Migration database
bench --site mihocm.dev migrate

# Build assets
bench --site mihocm.dev build

# Khởi động server
bench start
```

### Cài đặt chi tiết
Xem [Hướng dẫn cài đặt](docs/installation_guide.md) để biết thêm chi tiết.

## 📚 Tài liệu

- 📖 [Hướng dẫn cài đặt](docs/installation_guide.md)
- 🏗️ [Hướng dẫn tạo Workspace](docs/workspace_guide.md)
- 📋 [Tài liệu DocTypes](docs/doctypes_documentation.md)
- 🛠️ [Hướng dẫn tạo DocType](docs/doctype_creation_guide.md)
- 📚 [Tài liệu đầy đủ](docs/README.md)

## 🏗️ Cấu trúc dự án

```
mihocm/
├── mihocm/
│   ├── doctype/           # Tất cả DocTypes
│   │   ├── project/
│   │   ├── category/
│   │   ├── task/
│   │   ├── member/
│   │   ├── daily_progress_log/
│   │   ├── daily_resource_log/
│   │   └── daily_log_photo/
│   ├── config/            # Cấu hình app
│   ├── public/            # Assets tĩnh
│   └── www/               # Portal pages
├── docs/                  # Tài liệu
└── README.md
```

## 🔄 Workflow chính

1. **Tạo dự án** → Project
2. **Phân hạng mục** → Category
3. **Tạo đầu việc** → Task
4. **Thêm thành viên** → Member
5. **Báo cáo tiến độ** → Daily Progress Log
6. **Quản lý nguồn lực** → Daily Resource Log

## 📊 Trạng thái phát triển

- ✅ **DocTypes**: Hoàn thành 100%
- ✅ **Database**: Migration thành công
- ✅ **Workspace**: Đã tạo và cấu hình
- 🔄 **UI/UX**: Đang phát triển
- 🔄 **Mobile App**: Kế hoạch
- 🔄 **Reports**: Kế hoạch

## 🤝 Đóng góp

1. Fork repository
2. Tạo feature branch
3. Commit changes
4. Push to branch
5. Tạo Pull Request

## 📄 License

MIT License - Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

## 📞 Liên hệ

- **Developer**: Miho CM Team
- **Email**: support@mihocm.com
- **Version**: 1.0.0

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/mihocm
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.

### License

mit