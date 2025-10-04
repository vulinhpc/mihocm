import os

from . import __version__ as app_version

app_name = "mihocm"
app_title = "Miho Construction Management"
app_publisher = "Linh Vu"
app_description = "Miho construction management system"
app_email = "mrlinhvu1987@gmail.com"
app_license = "MIT"
app_logo_url = "/assets/mihocm/images/mihocm-logo.svg"
develop_version = "0.0.1-develop"

# Modules
# ------------------
app_modules = [
    "project",
    "category", 
    "task",
    "member",
    "daily_progress_log",
    "daily_resource_log",
    "daily_log_photo"
]

# Website
# ------------------
app_include_js = []
app_include_css = []
app_include_icons = []

# DocType JS
doctype_js = {}

# Website
web_include_js = []
web_include_css = []

# Email
email_css = []

# Website Route Rules
website_route_rules = []

# Website Redirects
website_redirects = []

# Base Template
base_template = "templates/base.html"

# Write File Keys
write_file_keys = []

# Notification Config
notification_config = "frappe.core.notifications.get_notification_config"

# Before Tests
before_tests = None

# Email Append To
email_append_to = []

# Calendars
calendars = []

# Leaderboards
leaderboards = None

# Login
on_session_creation = []
on_login = None
on_logout = None

# PDF
pdf_header_html = None
pdf_body_html = None
pdf_footer_html = None

# Permissions
permission_query_conditions = {}

# Scheduler Events
scheduler_events = {}

# Fixtures
fixtures = []

# Auto Update
auto_update = False

# Update
update = None

# Before Install
before_install = None

# After Install
after_install = None

# Before Uninstall
before_uninstall = None

# After Uninstall
after_uninstall = None