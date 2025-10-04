# Frappe App Documentation - Tài Liệu Chuẩn Thực Tế

## 🚨 **CẢNH BÁO QUAN TRỌNG**

Tài liệu chính thức của Frappe **CÓ NHIỀU LỖI VÀ THIẾU SÓT**. Bộ tài liệu này được viết dựa trên:

- ✅ **Kinh nghiệm thực tế** phát triển app
- ✅ **Phân tích cấu trúc ERPNext** (app chuẩn)
- ✅ **Test và verify** tất cả hướng dẫn
- ✅ **Troubleshooting** các lỗi thường gặp

## 📚 **DANH SÁCH TÀI LIỆU**

### **1. [Cấu Trúc App Chuẩn](./FRAPPE_APP_STRUCTURE_GUIDE.md)**
- Cấu trúc thư mục đúng chuẩn Frappe
- Các lỗi thường gặp và cách sửa
- Hướng dẫn tạo app từ đầu
- So sánh với ERPNext

### **2. [Template hooks.py](./HOOKS_PY_TEMPLATE.md)**
- Template hooks.py đầy đủ và chuẩn
- Giải thích từng trường bắt buộc
- Các lỗi thường gặp và cách sửa
- Ví dụ thực tế

### **3. [Hướng Dẫn Sửa Lỗi](./TROUBLESHOOTING_GUIDE.md)**
- Các lỗi thường gặp khi phát triển app
- Cách debug và sửa lỗi
- Checklist sửa lỗi
- Công cụ debug

### **4. [Best Practices](./BEST_PRACTICES.md)**
- Thực hành tốt nhất khi phát triển app
- Cấu trúc code chuẩn
- Workflow phát triển
- Performance tips

## 🎯 **TẠI SAO TÀI LIỆU NÀY CẦN THIẾT?**

### **Vấn đề với tài liệu chính thức:**
- ❌ **Thiếu thông tin** quan trọng
- ❌ **Có lỗi** và mâu thuẫn
- ❌ **Không test** các ví dụ
- ❌ **Thiếu troubleshooting**
- ❌ **Không cập nhật** theo phiên bản mới

### **Ưu điểm của tài liệu này:**
- ✅ **Đầy đủ** tất cả thông tin cần thiết
- ✅ **Chính xác** và đã test thực tế
- ✅ **Có ví dụ** cụ thể và thực tế
- ✅ **Troubleshooting** chi tiết
- ✅ **Cập nhật** theo kinh nghiệm thực tế

## 🚀 **CÁCH SỬ DỤNG**

### **1. Tạo app mới**
```bash
# Đọc hướng dẫn cấu trúc app
cat docs/FRAPPE_APP_STRUCTURE_GUIDE.md

# Tạo app theo hướng dẫn
bench new-app your_app_name
```

### **2. Cấu hình hooks.py**
```bash
# Sử dụng template chuẩn
cp docs/HOOKS_PY_TEMPLATE.md your_app/hooks.py

# Sửa thông tin app
# Test migration
bench --site your_site migrate
```

### **3. Sửa lỗi**
```bash
# Đọc hướng dẫn sửa lỗi
cat docs/TROUBLESHOOTING_GUIDE.md

# Tìm lỗi tương tự
# Áp dụng giải pháp
```

### **4. Phát triển app**
```bash
# Đọc best practices
cat docs/BEST_PRACTICES.md

# Áp dụng các thực hành tốt
# Test và verify
```

## 🔍 **CÁC LỖI THƯỜNG GẶP**

### **1. ModuleNotFoundError**
- **Nguyên nhân:** Cấu trúc app sai
- **Giải pháp:** Đọc [Cấu Trúc App Chuẩn](./FRAPPE_APP_STRUCTURE_GUIDE.md)

### **2. DocType không migrate**
- **Nguyên nhân:** hooks.py thiếu cấu hình
- **Giải pháp:** Đọc [Template hooks.py](./HOOKS_PY_TEMPLATE.md)

### **3. Website lỗi 500**
- **Nguyên nhân:** App có lỗi cấu trúc
- **Giải pháp:** Đọc [Hướng Dẫn Sửa Lỗi](./TROUBLESHOOTING_GUIDE.md)

## 📋 **CHECKLIST TẠO APP**

### **Trước khi bắt đầu:**
- [ ] Đọc tất cả tài liệu trong docs/
- [ ] Hiểu cấu trúc app chuẩn
- [ ] Chuẩn bị template hooks.py
- [ ] Backup dữ liệu hiện tại

### **Khi tạo app:**
- [ ] Tạo cấu trúc thư mục đúng
- [ ] Sử dụng template hooks.py chuẩn
- [ ] Tạo modules trong thư mục modules/
- [ ] Tạo DocTypes trong thư mục doctype/
- [ ] Test migration sau mỗi thay đổi

### **Sau khi hoàn thành:**
- [ ] Test tất cả chức năng
- [ ] Kiểm tra DocTypes trong database
- [ ] Test trên môi trường khác
- [ ] Viết tài liệu sử dụng

## 🚨 **LƯU Ý QUAN TRỌNG**

1. **Không tin tài liệu chính thức** - test thực tế
2. **Luôn backup** trước khi thay đổi
3. **Test migration** sau mỗi thay đổi
4. **Tham khảo ERPNext** để hiểu cấu trúc chuẩn
5. **Ghi lại các lỗi** để tránh lặp lại

## 📞 **HỖ TRỢ**

Nếu gặp vấn đề không có trong tài liệu:

1. **Kiểm tra lại** tất cả bước trong tài liệu
2. **Tìm kiếm** lỗi tương tự trong troubleshooting
3. **Tham khảo** cấu trúc ERPNext
4. **Test** trên môi trường mới

## 📚 **TÀI LIỆU THAM KHẢO**

- [ERPNext GitHub](https://github.com/frappe/erpnext) - App chuẩn
- [Frappe Framework](https://github.com/frappe/frappe) - Framework core
- [Frappe School](https://frappe.school/) - Học Frappe
- [Frappe Forum](https://discuss.frappe.io/) - Cộng đồng

---

**Lưu ý:** Bộ tài liệu này được viết dựa trên kinh nghiệm thực tế và phân tích cấu trúc ERPNext. Tài liệu chính thức của Frappe có nhiều lỗi và thiếu sót nghiêm trọng.

**Phiên bản:** 1.0.0  
**Cập nhật:** 2025-10-04  
**Tác giả:** Dựa trên kinh nghiệm thực tế phát triển app mihocm