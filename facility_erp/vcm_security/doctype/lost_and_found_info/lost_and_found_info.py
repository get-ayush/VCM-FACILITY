# Copyright (c) 2026, Ayush and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
from datetime import datetime


class LostAndFoundInfo(Document):

    def autoname(self):

        month_year = datetime.now().strftime("%m%y")

        generated_name = make_autoname(
            f"LF-{month_year}-.####"
        )

        self.name = generated_name

        self.lost_found_ticket = generated_name