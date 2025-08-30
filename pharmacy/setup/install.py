import frappe

def run_migration():
    seed_data()
    register_rest_api()

def seed_data():
    
    territories = ["UAE", "Dubai"]
    for name in territories:
        if not frappe.db.exists("Territory", name):
            frappe.get_doc({
                "doctype": "Territory",
                "territory_name": name,
                "is_group": 0
            }).insert()

    if not frappe.db.exists("Supplier", "Default Supplier"):
        frappe.get_doc({
            "doctype": "Supplier",
            "supplier_name": "Default Supplier",
            "supplier_type": "Company"
        }).insert()

def register_rest_api():
    # REST endpoints are exposed via whitelisted methods.
    # This function is a placeholder for future route registration if needed.
    pass
