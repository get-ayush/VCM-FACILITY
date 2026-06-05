// Copyright (c) 2026, Ayush and contributors
// For license information, please see license.txt

// Copyright (c) 2026, VCM Security Module
// Pattern: Comprehensive Multi-Section Data Fetch
// Copyright (c) 2026, VCM Security Module
// Pattern: Precise Multi-Section Asset Claim Data Fetch

frappe.ui.form.on('Asset Claim', {
    // 1. Trigger the script whenever 'lost_and_found_id' updates
    lost_and_found_id: function(frm) {
        
        // Step 1: If the user clears the 'lost_and_found_id' field, completely wipe out all target sections
        if (!frm.doc.lost_and_found_id) {
            frm.set_value({
                // Lost Found Section
                lost_date: '',
                lost_time: '',
                lf_status: '',
                
                // Finder Section
                finder_type: '',
                informed_by: '',
                
                // Asset Details Section
                asset_name: '',
                location: '',
                asset_image: ''
            });
            return;
        }

        // Step 2: Fetch the 8 precise fields using your single, verified 'lost_and_found_id' field value
        frappe.db.get_value('Lost And Found Info', frm.doc.lost_and_found_id, [
            'lost_date', 'lost_time', 'lf_status',    // Section 1
            'finder_type', 'informed_by',             // Section 2
            'asset_name', 'location', 'asset_image'   // Section 3
        ]).then(r => {
            if (r && r.message) {
                // Step 3: Map and populate the precise database entries directly into the UI sections
                frm.set_value({
                    // Lost Found Section
                    lost_date: r.message.lost_date,
                    lost_time: r.message.lost_time,
                    lf_status: r.message.lf_status,
                    
                    // Finder Section
                    finder_type: r.message.finder_type,
                    informed_by: r.message.informed_by,
                    
                    // Asset Details Section
                    asset_name: r.message.asset_name,
                    location: r.message.location,
                    asset_image: r.message.asset_image
                });
                
                // Fixed Status Check: Triggers a message if the fetched 'lf_status' from the source is 'Claimed'
                if (r.message.lf_status === 'Claimed') {
                    frappe.msgprint({
                        title: __('Attention'),
                        indicator: 'orange',
                        message: __('This Lost & Found record is already marked as Claimed.')
                    });
                }
            }
        });
    }
}); 