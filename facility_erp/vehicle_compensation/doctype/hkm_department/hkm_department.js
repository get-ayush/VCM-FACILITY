frappe.ui.form.on('HKM Department', {
    onload(frm) {
        if (frm.doc.name && !frm.doc.department_id) {
            frm.set_value('department_id', frm.doc.name);
        }
    }
});