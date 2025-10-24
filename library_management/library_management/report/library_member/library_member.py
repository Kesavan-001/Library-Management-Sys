import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": "Library Member", "fieldname": "name", "fieldtype": "Data", "width": 200},
        {"label": "Name", "fieldname": "name1", "fieldtype": "Data", "width": 200},
        {"label": "Email", "fieldname": "email", "fieldtype": "Data", "width": 300},
        {"label": "Mobile No", "fieldname": "mobile_no", "fieldtype": "Data", "width": 200},
    ]

def get_data(filters):
    conditions = []
    
    # Filter by Name if provided
    if filters.get("name1"):
        conditions.append(f"name1 LIKE '%{filters.get('name1')}%'")
    if filters.get("email"):
        conditions.append(f"email LIKE '%{filters.get('email')}%'")
 
    where_clause = " AND ".join(conditions)
    if where_clause:
        where_clause = "WHERE " + where_clause

    query = f"""
        SELECT
            name,
            name1,
            email,
            mobile_no
        FROM `tabLibrary Member`
        {where_clause};
    """
    return frappe.db.sql(query, as_dict=True)
