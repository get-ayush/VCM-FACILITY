# Copyright (c) 2026, Ayush and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
from datetime import datetime


class AssetLostComplaint(Document):

    def autoname(self):

        month_year = datetime.now().strftime("%m%y")

        generated_name = make_autoname(
            f"LA-{month_year}-.####"
        )

        self.name = generated_name

        self.lost_asset_id = generated_name
