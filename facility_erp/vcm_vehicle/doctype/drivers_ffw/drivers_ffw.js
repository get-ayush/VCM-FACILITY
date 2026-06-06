// Copyright (c) 2026, Ayush and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Drivers FFW", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Drivers FFW', {

    refresh(frm) {
        calculate_ffw_total(frm);
    },

    validate(frm) {
        calculate_ffw_total(frm);
    }
});

function calculate_ffw_total(frm) {

    let grand_total = 0;

    (frm.doc.ffw_details || []).forEach(row => {

        let row_total = 0;

        if (row.breakfast) row_total += 60;
        if (row.lunch) row_total += 85;
        if (row.tea) row_total += 20;
        if (row.night_charge) row_total += 100;

        row.total = row_total;

        grand_total += row_total;
    });

    frm.refresh_field("ffw_details");

    frm.set_value("ffw_value", grand_total);

    frm.refresh_field("ffw_value");
}