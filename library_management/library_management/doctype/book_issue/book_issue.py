import frappe
from frappe.model.document import Document
from frappe.utils import getdate

class BookIssue(Document):
    def validate(self):
        if not self.return_date:
            self.status = "Issued"           
        elif self.return_date and self.due_date:
            return_date = getdate(self.return_date)
            due_date = getdate(self.due_date)
              
            if return_date > due_date:
                fine = (return_date - due_date).days
                fine = fine * 10
                self.custom_fine = fine
                self.status = "Overdue"
            elif return_date == due_date: 
                self.status = "Returned"
        
        doc = frappe.get_doc("Books",self.book)
        avai = doc.available_copies  
        if avai == 0:  
            frappe.db.set_value("Books",self.book,"status","Not-Available")
            frappe.throw("Book Not Available")
            
        elif avai <= 10:
            if self.status == "Issued":        
                balance = avai - 1
                frappe.db.set_value("Books",self.book,"available_copies",balance)

            elif self.status == "Returned" or self.status == "Overdue":
                balance = avai + 1
                frappe.db.set_value("Books",self.book,"available_copies",balance)
             
                
    def before_save(self):
        
        doc = frappe.get_doc("Library Member",self.member)
        
        doc.append("book_details",{
                "book_name": self.book,
                "from_date": self.issue_date,
                "to_date": self.due_date,
                "return_date": self.return_date,
                "status": self.status
        })
        doc.save()

        
            