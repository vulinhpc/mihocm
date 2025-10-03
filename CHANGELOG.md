# Changelog

Tất cả các thay đổi quan trọng của dự án Miho Construction Management sẽ được ghi lại trong file này.

## [1.0.0] - 2025-10-03

### ✨ Added
- **DocTypes chính**:
  - `Project`: Quản lý thông tin dự án xây dựng
  - `Category`: Phân chia dự án thành các hạng mục
  - `Task`: Quản lý các đầu việc cụ thể
  - `Member`: Quản lý thành viên và vai trò dự án
  - `Daily Progress Log`: Báo cáo tiến độ cho khách hàng
  - `Daily Resource Log`: Quản lý nguồn lực nội bộ

- **Child DocTypes**:
  - `Daily Log Photo`: Lưu trữ ảnh minh chứng
  - `Daily Progress Log Task`: Liên kết tasks với nhật ký tiến độ
  - `Daily Resource Log Issue`: Ghi nhận vấn đề phát sinh

- **Tính năng**:
  - Workspace "Miho CM" với shortcuts cho tất cả DocTypes
  - Workflow approval cho Daily Progress Log
  - Hệ thống phân quyền theo vai trò (Owner/PM/Engineer/Supervisor/QC)
  - Tự động tính toán khối lượng thực tế từ Daily Resource Log

### 📚 Documentation
- Tài liệu chi tiết về tất cả DocTypes
- Hướng dẫn cài đặt và cấu hình
- Hướng dẫn tạo Workspace
- Hướng dẫn tạo DocType trong Frappe
- README.md với thông tin đầy đủ

### 🏗️ Technical
- Cấu trúc app theo chuẩn Frappe
- Tất cả DocTypes đã được migrate thành công
- Files được tổ chức trong `apps/mihocm/mihocm/doctype/`
- Cấu hình hooks.py và modules.txt hoàn chỉnh

### 🔧 Configuration
- Module: `mihocm`
- App: `mihocm`
- Database: MariaDB
- Framework: Frappe 15+

---

## [0.1.0] - 2025-10-03

### ✨ Added
- Khởi tạo dự án Miho Construction Management
- Cấu trúc cơ bản của Frappe app
- Workspace "Miho CM" cơ bản

---

## Format

Dự án này sử dụng [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
và dự án này tuân thủ [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
