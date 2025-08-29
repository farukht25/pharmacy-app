frappe.ui.form.on('Agency', {
    refresh(frm) {
        if (frm.doc.docstatus === 0 && frm.doc.is_active) {
            frm.add_custom_button('Create Supplier', () => {
                frappe.call({
                    method: 'pharmacy.agency_management.doctype.agency.agency.create_supplier',
                    args: { agency_name: frm.doc.name },
                    callback(r) {
                        frappe.msgprint(`Supplier ${r.message} created`);
                    }
                });
            });
        }
    }
});
