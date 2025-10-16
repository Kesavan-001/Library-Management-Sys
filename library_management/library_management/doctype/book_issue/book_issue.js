// Copyright (c) 2025, Kesavan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Book Issue", {
	refresh: function(frm) {

        frm.add_custom_button("Generate Fine",()=>
        
            frappe.new_doc("Fine",{
                member: frm.doc.member,
                name1:frm.doc.custom_name,
                book:frm.doc.book,
                amount:frm.doc.custom_fine

            })

        )

	},
    issue_date : function(frm){

        frappe.call({
            method:"frappe.client.get",
            args: {
                doctype:"Library Member",
                name: frm.doc.member
            },
            callback: function(r){
                if(r.message) {
                    let doc = r.message;
                    var start = new Date(doc.membership_start_date)
                    var end = new Date(doc.membership_end_date)

                    var issue = new Date(frm.doc.issue_date)

                    if(issue >= start && issue <= end ){
                        console.log("ok")

                    }
                    else{
                        frm.add_custom_button("Buy Membership",()=>{
                            frappe.new_doc("Membership Transaction",{
                                member:frm.doc.member
                            })
                        })
                    }
                    
                }
            }
        })

    }
})