import frappe
from frappe.model.document import Document

class ManufacturerItem(Document):
    def validate(self):
        # Block if manufacturer is marked as blocked
        if frappe.db.get_value("Pharmacy Manufacturer", self.manufacturer, "is_blocked"):
            frappe.throw(f"Cannot add items for blocked manufacturer: {self.manufacturer}")

        # Ensure uniqueness of (manufacturer, item_code)
        if frappe.db.exists("Manufacturer Item", {
            "manufacturer": self.manufacturer,
            "item_code": self.item_code,
            "name": ["!=", self.name]
        }):
            frappe.throw("This manufacturer-item mapping already exists.")

        # Auto-fill part_number if blank
        if not self.part_number:
            self.part_number = self.item_code

# @frappe.whitelist()
# def get_mappings_by_item(item_code):
#     return frappe.get_all("Manufacturer Item",
#         filters={"item_code": item_code},
#         fields=["manufacturer", "part_number", "gtin"])

@frappe.whitelist()
def get_mappings_by_item(item_code):
    return frappe.db.sql("""
        SELECT pm.manufacturer_name, mi.part_number, mi.gtin
        FROM `tabManufacturer Item` mi
        JOIN `tabPharmacy Manufacturer` pm ON pm.name = mi.manufacturer
        WHERE mi.item_code = %s AND pm.is_blocked = 0
    """, (item_code,), as_dict=True)
