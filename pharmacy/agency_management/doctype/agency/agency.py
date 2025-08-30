import frappe
from frappe.model.document import Document

class Agency(Document):
    def validate(self):
        if not self.is_active and self.agency_items:
            frappe.throw("Cannot deactivate agency with linked items.")

    def get_indicator(self):
        if not self.is_active:
            return ("Inactive", "red", "is_active,=,0")
        return ("Active", "green", "is_active,=,1")
    
    
    
    @staticmethod
    def get_list_fields():
        # This method ensures 'is_active' is always fetched for the list view
        return ["name", "is_active", "creation", "modified"]

@frappe.whitelist()
def create_supplier(agency_name):
    agency = frappe.get_doc("Agency", agency_name)
    supplier = frappe.new_doc("Supplier")
    supplier.supplier_name = agency.agency_name
    supplier.supplier_type = "Company"  
    supplier.save()
    return supplier.name

