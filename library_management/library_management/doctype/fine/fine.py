# Copyright (c) 2025, Kesavan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Fine(Document):
    def validate(self):
        if self.paid:
            doc = frappe.get_list("Book Issue",filters={"member":self.member, "status":["!=","Returned"]},fields=["name"])
            for row in doc:
                data = frappe.get_doc("Book Issue",row.name)
                # frappe.msgprint(data.member)
                # # data.status = "Returned"
                frappe.db.set_value("Book Issue", row.name, "status", "Returned")
                
    def on_submit(self):
        
        if self.paid:
            doc = frappe.get_doc("Library Member",self.member)
        
            for row in doc.fine_details:
                if row.fine_date == self.date_of_fine:
                    frappe.throw(f"A fine already exists for {self.date_of_fine}")

            # If loop completes with no throw, then append
            doc.append("fine_details", {
                "fine_date": self.date_of_fine,
                "amount": self.amount,
                "reason": self.reason
            })
            doc.save()
