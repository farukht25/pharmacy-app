# 📦 Pharmacy Management App (Frappe 15)

A custom Frappe 15 app for managing pharmacy operations, including inventory, manufacturer mappings, and reporting. Built with modular DocTypes, REST APIs, and fixtures for easy deployment.

## 🚀 Features

- Manufacturer–Item mapping via REST API
- Validated DocTypes for robust data entry
- Custom reports with Script Report fallback
- Exported fixtures for portability
- Token-based authentication for secure API access

## 🛠️ Installation

```bash
# Get Frappe bench ready
bench init my-bench --frappe-branch version-15
cd my-bench
bench new-site nexterp.test
bench get-app pharmacy_app https://github.com/farukht25/pharmacy_app.git
bench --site nexterp.test install-app pharmacy_app
