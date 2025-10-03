# Miho Construction Management

Miho Construction Management (Miho CM) là ứng dụng quản lý xây dựng được phát triển trên nền tảng Frappe Framework, cung cấp các tính năng quản lý dự án, nhân viên, khách hàng và vật liệu xây dựng.

## Tính năng chính

- 📁 **Quản lý dự án**: Theo dõi tiến độ và chi phí dự án
- ✅ **Quản lý công việc**: Phân công và theo dõi tasks
- 👥 **Quản lý khách hàng**: Thông tin và lịch sử khách hàng
- 👤 **Quản lý nhân viên**: Hồ sơ và phân quyền nhân viên
- 📦 **Quản lý vật liệu**: Kho và cung ứng vật liệu
- 🏗️ **Workspace tùy chỉnh**: Giao diện được tối ưu cho ngành xây dựng

## Cài đặt

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

## Tài liệu

- 📖 [Hướng dẫn cài đặt](docs/installation_guide.md)
- 🏗️ [Hướng dẫn tạo Workspace](docs/workspace_guide.md)
- 📚 [Tài liệu đầy đủ](docs/README.md)

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
