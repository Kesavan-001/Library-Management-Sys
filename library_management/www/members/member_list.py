import frappe

def get_context(context):
    context.members = frappe.get_all(
        "Library Member",
        fields=["name", "name1", "email", "mobile_no", "membership_start_date", "membership_end_date"],
        order_by="creation desc"
    )
    context.total_members = len(context.members)
