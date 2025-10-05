from . import __version__ as app_version

app_name = "mihocm"
app_title = "MihoCM"
app_publisher = "Linh Vu"
app_description = "Miho construction management"
app_email = "mrlinhvu1987@gmail.com"
app_license = "MIT"
app_version = app_version

# Includes in <head>
# ------------------
# app_include_css = "/assets/mihocm/css/mihocm.css"
# app_include_js = "/assets/mihocm/js/mihocm.js"

# Home Pages
# ----------
# home_page = "login"

# Generators
# ----------
# website_generators = ["Web Page"]

# Installation
# ------------
# before_install = "mihocm.install.before_install"
# after_install = "mihocm.install.after_install"

# Uninstallation
# --------------
# before_uninstall = "mihocm.uninstall.before_uninstall"
# after_uninstall = "mihocm.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# notification_config = "mihocm.notifications.get_notification_config"

# Permissions
# -----------
# permission_query_conditions = {
#     "DocType": "mihocm.doctype.doctype.doctype.get_permission_query_conditions",
# }
# has_permission = {
#     "DocType": "mihocm.doctype.doctype.doctype.has_permission",
# }

# DocType Class Overrides
# -----------------------
# override_doctype_class = {
#     "ToDo": "mihocm.overrides.custom_todo.CustomToDo"
# }

# Document Events
# ---------------
# doc_events = {
#     "DocType": {
#         "on_update": "method",
#         "on_cancel": "method",
#         "on_trash": "method",
#     }
# }

# Scheduled Tasks
# ---------------
# scheduler_events = {
#     "all": [
#         "mihocm.tasks.all"
#     ],
#     "daily": [
#         "mihocm.tasks.daily"
#     ],
#     "hourly": [
#         "mihocm.tasks.hourly"
#     ],
#     "weekly": [
#         "mihocm.tasks.weekly"
#     ],
#     "monthly": [
#         "mihocm.tasks.monthly"
#     ],
# }

# Testing
# -------
# before_tests = "mihocm.tests.before_tests"

# Overriding Methods
# ------------------
# override_whitelisted_methods = {
#     "frappe.desk.doctype.event.event.get_events": "mihocm.event.get_events"
# }

# doctype_js = {
#     "DocType": "public/js/doctype.js"
# }

# doctype_list_js = {
#     "DocType": "public/js/doctype_list.js"
# }

# doctype_tree_js = {
#     "DocType": "public/js/doctype_tree.js"
# }

# doctype_calendar_js = {
#     "DocType": "public/js/doctype_calendar.js"
# }

# Auto cancel old doc types
# -------------------------
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# User Data Protection
# --------------------
# user_data_fields = [
#     {
#         "doctype": "DocType",
#         "filter_by": "name",
#         "redact_fields": ["fieldname"],
#         "partial": 1,
#     }
# ]

# Authentication and authorization
# --------------------------------
# auth_hooks = {
#     "validate": "mihocm.auth.validate"
# }

app_modules = ["MihoCM"]
