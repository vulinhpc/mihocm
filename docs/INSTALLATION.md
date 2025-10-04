# 🚀 Hướng Dẫn Cài Đặt MihoCM

## 📋 Yêu Cầu Hệ Thống

### **Phần Mềm Cần Thiết**
- **Python**: 3.8+ 
- **Node.js**: 14+
- **MariaDB**: 10.3+
- **Redis**: 6.0+
- **Git**: 2.0+

### **Hệ Điều Hành**
- Ubuntu 20.04+ (Khuyến nghị)
- CentOS 7+
- macOS 10.15+
- Windows 10+ (WSL2)

## 🛠️ Cài Đặt Frappe Bench

### **1. Cài đặt các gói cần thiết (Ubuntu/Debian)**
```bash
# Cập nhật hệ thống
sudo apt update && sudo apt upgrade -y

# Cài đặt các gói cần thiết
sudo apt install -y python3-dev python3-pip python3-venv \
    python3-setuptools python3-wheel \
    git curl wget \
    mariadb-server mariadb-client \
    redis-server \
    nginx \
    supervisor \
    libmysqlclient-dev \
    pkg-config \
    build-essential
```

### **2. Cài đặt Node.js**
```bash
# Cài đặt Node.js 18.x
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Kiểm tra phiên bản
node --version
npm --version
```

### **3. Cài đặt Frappe Bench**
```bash
# Cài đặt bench
sudo pip3 install frappe-bench

# Tạo thư mục bench
mkdir -p ~/frappe-bench
cd ~/frappe-bench

# Khởi tạo bench
bench init --frappe-branch version-14 frappe-bench
cd frappe-bench
```

## 🏗️ Cài Đặt MihoCM

### **1. Tạo site mới**
```bash
# Tạo site
bench new-site [site_name]
# Ví dụ: bench new-site mihocm.local

# Cài đặt app mihocm
bench get-app mihocm
```

### **2. Cài đặt app vào site**
```bash
# Cài app mihocm vào site
bench --site [site_name] install-app mihocm

# Migrate database
bench --site [site_name] migrate
```

### **3. Khởi động bench**
```bash
# Khởi động tất cả services
bench start

# Hoặc khởi động trong background
bench start --daemon
```

## 🌐 Truy Cập Ứng Dụng

### **1. Truy cập qua trình duyệt**
```
http://[site_name]:8000
# Ví dụ: http://mihocm.local:8000
```

### **2. Đăng nhập**
- **Username**: Administrator
- **Password**: [password đã thiết lập khi tạo site]

## 🔧 Cấu Hình Nâng Cao

### **1. Cấu hình Nginx (Tùy chọn)**
```bash
# Tạo file cấu hình Nginx
sudo nano /etc/nginx/sites-available/[site_name]

# Nội dung file:
server {
    listen 80;
    server_name [site_name];
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

# Kích hoạt site
sudo ln -s /etc/nginx/sites-available/[site_name] /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### **2. Cấu hình SSL (Tùy chọn)**
```bash
# Cài đặt Certbot
sudo apt install certbot python3-certbot-nginx

# Tạo chứng chỉ SSL
sudo certbot --nginx -d [site_name]
```

## 🐛 Xử Lý Lỗi Thường Gặp

### **1. Lỗi cài đặt Python packages**
```bash
# Cập nhật pip
pip3 install --upgrade pip

# Cài đặt lại requirements
pip3 install -r requirements.txt
```

### **2. Lỗi MariaDB**
```bash
# Khởi động MariaDB
sudo systemctl start mariadb
sudo systemctl enable mariadb

# Cấu hình bảo mật
sudo mysql_secure_installation
```

### **3. Lỗi Redis**
```bash
# Khởi động Redis
sudo systemctl start redis-server
sudo systemctl enable redis-server

# Kiểm tra trạng thái
sudo systemctl status redis-server
```

### **4. Lỗi Node.js packages**
```bash
# Xóa node_modules và cài lại
rm -rf node_modules
npm install

# Hoặc sử dụng yarn
yarn install
```

## 📊 Kiểm Tra Cài Đặt

### **1. Kiểm tra DocTypes**
```bash
# Vào console
bench --site [site_name] console

# Trong console, chạy:
frappe.db.sql('SELECT name FROM tabDocType WHERE module = "mihocm"')
```

### **2. Kiểm tra Tables**
```bash
# Kiểm tra tables trong database
bench --site [site_name] mariadb
# Trong MariaDB:
SHOW TABLES LIKE 'tab%';
```

### **3. Kiểm tra Logs**
```bash
# Xem logs bench
bench --site [site_name] logs

# Xem logs cụ thể
bench --site [site_name] logs --type error
```

## 🚀 Triển Khai Production

### **1. Cấu hình Production**
```bash
# Tạo site production
bench new-site [production_site] --mariadb-root-password [password]

# Cài đặt app
bench --site [production_site] install-app mihocm

# Migrate
bench --site [production_site] migrate
```

### **2. Cấu hình Supervisor**
```bash
# Tạo file cấu hình supervisor
sudo nano /etc/supervisor/conf.d/frappe.conf

# Nội dung:
[program:frappe]
command=bench start --daemon
directory=/home/[user]/frappe-bench
user=[user]
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/frappe.log

# Khởi động lại supervisor
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start frappe
```

## 📞 Hỗ Trợ

Nếu gặp vấn đề trong quá trình cài đặt:

1. **Kiểm tra logs**: `bench --site [site_name] logs`
2. **Tạo issue**: Trên GitHub repository
3. **Liên hệ**: mrlinhvu1987@gmail.com

---

**Chúc bạn cài đặt thành công!** 🎉