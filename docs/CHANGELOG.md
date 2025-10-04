# Changelog - Miho Construction Management App

## [1.1.0] - 2025-10-04

### 🔧 Fixed
- **CRITICAL**: Fixed module structure to prevent `ModuleNotFoundError`
- **CRITICAL**: Fixed module name conflict with Frappe core
- **CRITICAL**: Moved DocTypes to correct module structure
- Fixed `modules.txt` format to list only module names
- Fixed `hooks.py` configuration
- Added proper `__init__.py` files

### 📁 Structure Changes
- Moved all DocTypes from `doctype/` to `mihocm/` module
- Removed duplicate module directories
- Cleaned up unnecessary files
- Standardized module naming convention

### 📚 Documentation
- Added comprehensive README.md
- Added detailed INSTALLATION.md
- Added troubleshooting guide
- Added changelog

### ✅ Installation
- App now installs successfully on first attempt
- No manual fixes required after installation
- Compatible with Frappe v14+
- Tested on fresh Frappe installations

## [1.0.0] - 2025-10-03

### 🎉 Initial Release
- Basic project management functionality
- DocTypes: Project, Category, Task, Member
- Daily logging: Progress Log, Resource Log, Photos
- Basic CRUD operations
- Frappe Framework integration

### 🐛 Known Issues (Fixed in 1.1.0)
- Module structure caused installation failures
- Module name conflicts with Frappe core
- DocTypes not properly organized
- Required manual fixes after installation

## Migration Notes

### From v1.0.0 to v1.1.0
If upgrading from v1.0.0:

1. **Backup your data**:
   ```bash
   bench --site [SITE_NAME] backup
   ```

2. **Uninstall old version**:
   ```bash
   bench --site [SITE_NAME] uninstall-app mihocm
   ```

3. **Install new version**:
   ```bash
   bench get-app https://github.com/vulinhpc/mihocm.git --force
   bench --site [SITE_NAME] install-app mihocm
   bench --site [SITE_NAME] migrate
   ```

4. **Restore data** (if needed):
   ```bash
   bench --site [SITE_NAME] restore [BACKUP_FILE]
   ```

## Breaking Changes

### v1.1.0
- **Module structure**: DocTypes moved from `doctype/` to `mihocm/`
- **Module naming**: Standardized module names in `modules.txt`
- **File organization**: Cleaned up duplicate directories

## Compatibility

### Frappe Framework
- ✅ v14.0+
- ✅ v15.0+ (expected)
- ❌ v13.x and below

### Python
- ✅ 3.8+
- ✅ 3.9+
- ✅ 3.10+
- ❌ 3.7 and below

### Database
- ✅ MariaDB 10.3+
- ✅ MariaDB 10.4+
- ✅ MariaDB 10.5+
- ❌ MySQL 5.7 and below

## Testing

### Tested Scenarios
- ✅ Fresh Frappe installation
- ✅ Fresh site creation
- ✅ App installation
- ✅ Database migration
- ✅ DocType creation
- ✅ Module loading
- ✅ Server startup

### Test Commands
```bash
# Test app installation
bench get-app https://github.com/vulinhpc/mihocm.git
bench --site [SITE_NAME] install-app mihocm

# Test module loading
bench --site [SITE_NAME] console
>>> import mihocm
>>> frappe.get_list('DocType', filters={'module': 'mihocm'})

# Test server startup
bench start
# Check: http://localhost:8000
```

## Future Plans

### v1.2.0 (Planned)
- Enhanced project dashboard
- Advanced reporting features
- Mobile app integration
- API endpoints for external access

### v2.0.0 (Planned)
- Multi-tenant support
- Advanced workflow management
- Integration with external systems
- Performance optimizations
