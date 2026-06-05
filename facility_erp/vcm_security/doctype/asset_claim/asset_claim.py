# # Copyright (c) 2026, Ayush and contributors
# # For license information, please see license.txt

# # import frappe
# # -*- coding: utf-8 -*-
# # Copyright (c) 2026, VCM Security Module
# # Operational Requirement: Absolute 1:1 Primary Key Sync Mapping

# import frappe
# from frappe.model.document import Document
# from frappe import _

# class AssetClaim(Document):
# 	def autoname(self):
# 		"""
# 		Intercepts creation right before saving. 
# 		Copies the exact string value inside 'lost_and_found_id' and assigns 
# 		it directly as the primary unique ID ('name') of the Asset Claim document.
# 		"""
# 		# Confirm the link ID input is active and populated
# 		if getattr(self, "lost_and_found_id", None):
			
# 			# Extract the exact string value from your form field
# 			exact_source_id = str(self.lost_and_found_id).strip()
			
# 			# Fallback validation check: Stop if this exact ID has already been claimed
# 			if frappe.db.exists("Asset Claim", exact_source_id):
# 				frappe.throw(
# 					msg=_("An Asset Claim document with ID <b>{0}</b> already exists in the system.").format(exact_source_id),
# 					title=_("Duplicate Record Blocked")
# 				)
			
# 			# The exact copy assignment you asked for:
# 			self.name = exact_source_id
			
# 		else:
# 			# Safety block: Form cannot save without the source ID filled out
# 			frappe.throw(
# 				msg=_("Please select a valid 'Lost and Found ID' before attempting to save this form."),
# 				title=_("Missing Primary Reference")
# 			)

# # -*- coding: utf-8 -*-
# # Copyright (c) 2026, VCM Security Module
# # Operational Requirement: Sync Status Update Across Both Forms On Submission

# import frappe
# from frappe.model.document import Document
# from frappe import _

# class AssetClaim(Document):
#     def on_submit(self):
#         """
#         Executes automatically the split second the document is permanently Submitted.
#         Updates 'lf_status' to 'Claimed' in both Asset Claim and the original Lost And Found ticket.
#         """
#         # 1. Update the status on the current Asset Claim form
#         self.db_set('lf_status', 'Claimed')
        
#         # 2. Check if the link field 'lost_and_found_id' is populated
#         if self.lost_and_found_id:
#             # Check if the original Lost And Found document exists in the database
#             if frappe.db.exists("Lost And Found", self.lost_and_found_id):
                
#                 # Fetch the original parent document
#                 lf_doc = frappe.get_doc("Lost And Found", self.lost_and_found_id)
                
#                 # Update its status variable directly
#                 lf_doc.lf_status = "Claimed"
                
#                 # Add a system comment in its timeline so security guards can track who processed it
#                 lf_doc.add_comment(
#                     comment_type="Info",
#                     text=_("Asset status automatically updated to 'Claimed' via Asset Claim submission: {0}").format(self.name)
#                 )
                
#                 # Save the changes to the Lost And Found document
#                 lf_doc.save(ignore_permissions=True)
                
#                 # Pop up a clean confirmation message on the screen for the user
#                 frappe.msgprint({
#                     "title": _("Status Synchronized"),
#                     "message": _("Lost & Found Ticket <b>{0}</b> status successfully updated to 'Claimed'.").format(self.lost_and_found_id),
#                     "indicator": "green"
#                 })
#             else:
#                 frappe.throw(_("The linked Lost And Found record ({0}) could not be found to update its status.").format(self.lost_and_found_id))
# -*- coding: utf-8 -*-
# Copyright (c) 2026, VCM Security Module
# Operational Requirement: 1:1 ID Mapping + Automatic Status Sync

# -*- coding: utf-8 -*-
# Copyright (c) 2026, VCM Security Module
# Operational Requirement: 1:1 ID Mapping + Automatic Status Sync

import frappe
from frappe.model.document import Document
from frappe import _

class AssetClaim(Document):
    def autoname(self):
        """
        Runs BEFORE insert.
        Copies the exact 'lost_and_found_id' string to use as the primary key.
        """
        if getattr(self, "lost_and_found_id", None):
            exact_source_id = str(self.lost_and_found_id).strip()
            
            if frappe.db.exists("Asset Claim", exact_source_id):
                frappe.throw(
                    msg=_("An Asset Claim document with ID <b>{0}</b> already exists.").format(exact_source_id),
                    title=_("Duplicate Record Blocked")
                )
            
            # Set the primary document name to match the L&F ID
            self.name = exact_source_id
        else:
            frappe.throw(
                msg=_("Please select a valid 'Lost and Found ID' before saving."),
                title=_("Missing Primary Reference")
            )

    def on_submit(self):
        """
        Runs DURING submission.
        Updates 'lf_status' to 'Claimed' on BOTH forms automatically.
        """
        # 1. Force current Asset Claim status to Claimed
        self.db_set('lf_status', 'Claimed')
        
        # 2. Update the parent 'Lost And Found' record status automatically
        if self.lost_and_found_id:
            if frappe.db.exists("Lost And Found Info", self.lost_and_found_id):
                
                # FIX: Swapped 'doc' with 'self' so the database finds the ID variable perfectly
                frappe.db.set_value("Lost And Found Info", self.lost_and_found_id, "lf_status", "Claimed")
                
                # Add a timeline message to the original ticket for tracking
                lf_doc = frappe.get_doc("Lost And Found Info", self.lost_and_found_id)
                lf_doc.add_comment(
                    comment_type="Info",
                    text=_("Asset status automatically updated to 'Claimed' via Asset Claim submission: {0}").format(self.name)
                )