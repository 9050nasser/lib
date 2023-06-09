// Copyright (c) 2023, Mohammed Nasser and contributors
// For license information, please see license.txt

frappe.ui.form.on('Lib Library Member', {
    refresh: function(frm) {
        frm.add_custom_button('Create Membership', () => {
            frappe.new_doc('Lib Library Membership', {
                library_member: frm.doc.name
            })
        })
        frm.add_custom_button('Create Transaction', () => {
            frappe.new_doc('Lib Library Transaction', {
                library_member: frm.doc.name
            })
        })
    }
});

