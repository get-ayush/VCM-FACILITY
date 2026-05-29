# Copyright (c) 2026, Ayush and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document



class VehicleMaster(Document):

    def autoname(self):

        self.name = f"{self.vehicle_model} , {self.vehicle_no}"
