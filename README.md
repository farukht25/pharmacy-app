markdown
# 💊 Pharmacy Management App (Frappe 15)

A custom Frappe 15 app for managing pharmacy operations, including manufacturer–item mappings, validated DocTypes, and resilient reporting. Built with modular architecture and designed for easy deployment and API integration.

---

## 🚀 Features

- ✅ Manufacturer–Item mapping via REST API
- ✅ Validated DocTypes for robust data entry
- ✅ Script Reports for schema-resilient analytics
- ✅ Exported fixtures for portability
- ✅ Token-based authentication for secure API access

---

## 🧪 Development Environment

This app was developed inside a Python virtual environment to isolate dependencies.

### 🔧 Setup Instructions

```bash
# Create and activate virtual environment
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install Frappe Bench CLI
pip install frappe-bench

# Initialize bench and create site
bench init erp-bench --frappe-branch version-15
cd erp-bench
bench new-site pharmacy.local

# Get the app from GitHub and install it
bench get-app pharmacy_app https://github.com/yourusername/pharmacy_app.git
bench --site pharmacy.local install-app pharmacy_app
```

📦 Deployment
To deploy the app with fixtures:

bash
```
bench --site pharmacy.local migrate
bench --site pharmacy.local import-fixtures
```
▶️ Starting the App
Once installed, start the development server:

bash
```
cd erp-bench
bench start
```
Then open your browser and navigate to:

Code
http://localhost:8000

bash
pip install -r requirements.txt
