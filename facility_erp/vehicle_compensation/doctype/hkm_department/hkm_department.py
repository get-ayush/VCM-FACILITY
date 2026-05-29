# Copyright (c) 2026, Ayush and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HKMDepartment(Document):
    def before_save(self):
        self.department_id = self.name
	