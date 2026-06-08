# Copyright (c) 2026, Ayush and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
from datetime import datetime


class FacilityCostCentre(Document):

    def autoname(self):

        

        generated_name = make_autoname(
            f"FCC-.###"
        )

        self.name = generated_name

        self.cost_centre_id = generated_name