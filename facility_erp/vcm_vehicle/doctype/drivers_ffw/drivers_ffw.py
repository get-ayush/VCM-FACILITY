# Copyright (c) 2026, Ayush and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
from datetime import datetime

class DriversFFW(Document):

    def validate(self):

        grand_total = 0

        for row in self.ffw_details:

            row_total = 0

            if row.breakfast:
                row_total += 60

            if row.lunch:
                row_total += 85

            if row.tea:
                row_total += 20

            if row.night_charge:
                row_total += 100

            row.total = row_total
            grand_total += row_total

        self.ffw_value = grand_total





class DriversFFW(Document):

    def autoname(self):

        month_year = datetime.now().strftime("%m%y")

        generated_name = make_autoname(
            f"FFW-{month_year}-.###"
        )

        self.name = generated_name

        self.ffw_id = generated_name
