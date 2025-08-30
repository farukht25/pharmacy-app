# 💊 Pharmacy Management App (Frappe 15)

A custom Frappe 15 app for managing pharmacy operations, including manufacturer–item mappings, validated DocTypes, and resilient reporting. Built with modular architecture and designed for easy deployment and API integration.

---



## 🧪 Development Environment

This app was developed inside a Python virtual environment to isolate dependencies.

---

## 🔧 Setup Instructions

```bash
# Create and activate virtual environment
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Frappe Bench CLI
pip install frappe-bench

# Initialize bench and create site
bench init erp-bench --frappe-branch version-15
cd erp-bench
bench new-site pharmacy.local

# Get the app from GitHub and install it
bench get-app pharmacy_app https://github.com/farukht25/pharmacy_app.git
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
Log in using the admin credentials you set during bench new-site.


Testing

Module 1: Agency Management 

Search for  Agency List
<img width="953" height="527" alt="image" src="https://github.com/user-attachments/assets/88d16c35-11a6-411c-bbca-6058d1729549" />
click on add agencies 
<img width="950" height="485" alt="image" src="https://github.com/user-attachments/assets/212028b0-376a-403b-b219-d8860a128118" />
for active agencies check is active and add agency item
and for inactive agencies do not check is active 
if is active is unchecked and items are not linked, you won't be able to save the agency

for active agencies you can click on create supplier button to create new supplier 
<img width="929" height="487" alt="image" src="https://github.com/user-attachments/assets/32ee31cb-85eb-417c-8f31-71a32c2a9991" />
go to the search bar and type supplier type to view new supplier
<img width="954" height="464" alt="image" src="https://github.com/user-attachments/assets/f172104f-5f3f-4d78-b157-9408b0b0b32e" />

to view report, search for report list and click on Agency Lead Times and click on show result
<img width="952" height="461" alt="image" src="https://github.com/user-attachments/assets/6a51a944-dca5-4161-ac3b-066bb2b414e4" />

Module 2: Manufacturer–Item Mapping

search for Pharmacy Manufacturer List in the search bar
create two items, one with is blocked check and another one with is blocked unchecked
<img width="959" height="295" alt="image" src="https://github.com/user-attachments/assets/90013447-8fae-4d53-a1c6-379c7c94e4f3" />








