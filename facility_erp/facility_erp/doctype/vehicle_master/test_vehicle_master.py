# Copyright (c) 2026, Ayush and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase




class VehicleMaster(Document):

    def autoname(self):

        self.name = f"{self.vehicle_model} , {self.vehicle_no}"
