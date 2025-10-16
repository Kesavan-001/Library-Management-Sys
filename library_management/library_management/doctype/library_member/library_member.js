// Copyright (c) 2025, Kesavan and contributors
// For license information, please see license.txt

frappe.ui.form.on("Library Member", {
	refresh(frm) {
        
        let btn = document.querySelector('.btn.btn-xs.btn-secondary.grid-add-row')
        
        if (btn){
            btn.classList.add('hidden')
        }

	},
});
