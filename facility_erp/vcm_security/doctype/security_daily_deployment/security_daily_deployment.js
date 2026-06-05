// Copyright (c) 2026, Ayush and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Security Daily Deployment", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Security Daily Deployment', {

    setup(frm) {

        frm.fields_dict.deployment_details.grid.get_field('security_guards').get_query =
        function(doc) {

            return {
                filters: {
                    employee_type: doc.deployment_type
                }
            };
        };

    },

    deployment_type(frm) {
        frm.refresh_field('deployment_details');
    }

});