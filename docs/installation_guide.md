# Hướng dẫn cài đặt Miho CM App

## Tổng quan
Miho CM (Miho Construction Management) là ứng dụng quản lý xây dựng được phát triển trên nền tảng Frappe Framework.

## Yêu cầu hệ thống

### Phần mềm cần thiết
- Python 3.8+
- Node.js 14+
- MariaDB 10.3+
- Redis 6.0+
- Frappe Framework 15+

### Hệ điều hành
- Ubuntu 20.04+ (khuyến nghị)
- CentOS 8+
- Windows 10+ (với WSL2)

## Cài đặt

### 1. Chuẩn bị môi trường

```bash
# Cài đặt Python và pip
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Cài đặt Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Cài đặt MariaDB
sudo apt install mariadb-server mariadb-client

# Cài đặt Redis
sudo apt install redis-server
```

### 2. Cài đặt Frappe Bench

```bash
# Cài đặt frappe-bench
pip3 install frappe-bench

# Tạo bench mới
bench init frappe-bench --frappe-branch version-15

# Di chuyển vào thư mục bench
cd frappe-bench
```

### 3. Tạo site

```bash
# Tạo site mới
bench new-site mihocm.dev

# Cài đặt app mihocm
bench --site mihocm.dev install-app mihocm

# Migration database
bench --site mihocm.dev migrate

# Build assets
bench --site mihocm.dev build
```

### 4. Cấu hình Redis

Cập nhật file `sites/mihocm.dev/site_config.json`:

```json
{
  "db_name": "_dba46d1783b7cf05",
  "db_password": "your_db_password",
  "db_type": "mariadb",
  "redis_cache": "redis://127.0.0.1:13001",
  "redis_queue": "redis://127.0.0.1:11001",
  "redis_socketio": "redis://127.0.0.1:11001"
}
```

### 5. Khởi động server

```bash
# Khởi động tất cả services
bench start

# Hoặc khởi động riêng web server
bench --site mihocm.dev serve --port 8001
```

## Cấu hình

### 1. Cấu hình Database

```bash
# Tạo database user
mysql -u root -p
CREATE USER 'mihocm_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON *.* TO 'mihocm_user'@'localhost';
FLUSH PRIVILEGES;
```

### 2. Cấu hình Redis

Kiểm tra file cấu hình Redis:
- `config/redis_cache.conf`
- `config/redis_queue.conf`

### 3. Cấu hình Site

Chỉnh sửa `sites/mihocm.dev/site_config.json`:

```json
{
  "db_name": "mihocm_db",
  "db_password": "your_password",
  "db_type": "mariadb",
  "redis_cache": "redis://127.0.0.1:13001",
  "redis_queue": "redis://127.0.0.1:11001",
  "redis_socketio": "redis://127.0.0.1:11001",
  "maintenance_mode": 0,
  "developer_mode": 1
}
```

## Kiểm tra cài đặt

### 1. Kiểm tra services

```bash
# Kiểm tra Redis
redis-cli ping

# Kiểm tra MariaDB
mysql -u root -p -e "SHOW DATABASES;"

# Kiểm tra Frappe
bench --site mihocm.dev console
```

### 2. Kiểm tra web interface

Truy cập: `http://localhost:8001`

- Login: Administrator
- Password: (password đã set khi tạo site)

### 3. Kiểm tra app

```bash
# Kiểm tra app đã cài
bench --site mihocm.dev list-apps

# Kiểm tra workspace
bench --site mihocm.dev execute frappe.get_doc --args '["Workspace", "Miho CM"]'
```

## Troubleshooting

### Lỗi kết nối Redis

```bash
# Khởi động Redis
sudo systemctl start redis-server
sudo systemctl enable redis-server

# Kiểm tra port
netstat -tulnp | grep redis
```

### Lỗi kết nối Database

```bash
# Khởi động MariaDB
sudo systemctl start mariadb
sudo systemctl enable mariadb

# Kiểm tra kết nối
mysql -u root -p
```

### Lỗi cài đặt app

```bash
# Xóa app và cài lại
bench --site mihocm.dev uninstall-app mihocm
bench --site mihocm.dev install-app mihocm
bench --site mihocm.dev migrate
```

### Lỗi build assets

```bash
# Xóa cache và build lại
bench --site mihocm.dev clear-cache
bench --site mihocm.dev build
```

## Cập nhật

### Cập nhật app

```bash
# Cập nhật app
bench --site mihocm.dev update --patch

# Migration
bench --site mihocm.dev migrate

# Build assets
bench --site mihocm.dev build
```

### Cập nhật Frappe

```bash
# Cập nhật Frappe
bench update --patch

# Restart services
bench restart
```

## Backup và Restore

### Backup

```bash
# Backup database
bench --site mihocm.dev backup

# Backup files
bench --site mihocm.dev backup --with-files
```

### Restore

```bash
# Restore database
bench --site mihocm.dev restore backup_file.sql.gz

# Restore files
bench --site mihocm.dev restore backup_file.sql.gz --with-files
```

## Bảo mật

### 1. Cấu hình SSL

```bash
# Tạo SSL certificate
bench --site mihocm.dev setup-ssl

# Cấu hình nginx
bench setup-nginx
```

### 2. Cấu hình firewall

```bash
# Mở port cần thiết
sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow 8001
```

### 3. Cấu hình user

```bash
# Tạo user mới
bench --site mihocm.dev add-to-hosts
bench --site mihocm.dev set-admin-password new_password
```

## Monitoring

### 1. Log files

```bash
# Xem logs
tail -f logs/bench.log
tail -f logs/worker.log
tail -f logs/worker.error.log
```

### 2. Performance

```bash
# Kiểm tra performance
bench --site mihocm.dev doctor

# Kiểm tra database
bench --site mihocm.dev mariadb
```

## Liên hệ hỗ trợ

- **Email**: support@mihocm.com
- **Documentation**: [Miho CM Docs](https://docs.mihocm.com)
- **GitHub**: [Miho CM Repository](https://github.com/mihocm/mihocm)
