# Copyright (c) 2021, codescientist703 and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ChatMessage(Document):
	def change_column_type(self):
		frappe.db.change_column("Chat Message", "content", "Long Text")
		frappe.db.commit()
