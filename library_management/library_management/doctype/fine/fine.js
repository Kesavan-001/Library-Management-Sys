// Copyright (c) 2025, Kesavan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Fine", {

    refresh: function(frm){
        let field = frm.doc.paid
        if (field){
            frm.set_df_property("paid","hidden",1)
        }
        else{
            frm.set_df_property("paid","hidden",0)
        }
    }

});


// after_save: function(frm) {
//     frappe.call({
//         method: "frappe.client.get",
//         args: {
//             doctype: "Books",
//             name: frm.doc.book
//         },
//         callback: function(r) {
//             if (r.message) {
//                 let book_doc = r.message;
//                 frappe.msgprint("Available copies: " + book_doc.available_copies);
//             }
//         }
//     });
// }
