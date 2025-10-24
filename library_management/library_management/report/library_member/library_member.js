frappe.query_reports["Library Member"] = {
    "filters": [
        {
            "fieldname": "name1",
            "label": __("Name"),
            "fieldtype": "Data",
            "placeholder": "Enter name to filter"
        },
		{
			"fieldname":"email",
			"label":__("Email"),
			"fieldtype":"Data",
			"placeholder":"Enter Email to filter"
		}
    ]
};
