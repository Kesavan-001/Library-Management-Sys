# Copyright (c) 2025, Kesavan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class MembershipTransaction(Document):
        
    def on_change(self):
        frappe.db.set_value("Library Member",self.member,"membership_start_date",self.start_date)
        frappe.db.set_value("Library Member",self.member,"membership_end_date",self.end_date)

        
     
