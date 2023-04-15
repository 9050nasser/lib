# Copyright (c) 2023, Mohammed Nasser and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class LibLibraryMember(Document):
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'
