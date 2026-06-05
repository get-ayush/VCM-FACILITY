frappe.ui.form.on('Fuel Info', {
    quantity(frm) {
        calculate_amount(frm);
    },

    rate(frm) {
        calculate_amount(frm);
    }
});

function calculate_amount(frm) {
    frm.set_value(
        'amount_paid',
        (frm.doc.quantity || 0) * (frm.doc.rate || 0)
    );
}