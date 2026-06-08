# Copyright (c) 2026, Ayush and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
from datetime import datetime


class FacilityBudgetHead(Document):

    def autoname(self):

        

        generated_name = make_autoname(
            f"FBH-.###"
        )

        self.name = generated_name

        self.budget_head_id = generated_name