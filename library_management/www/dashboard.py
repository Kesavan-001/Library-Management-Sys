import frappe

def get_context(context):
    context.members = frappe.get_all(
        "Library Member",
        fields=["name", "name1", "email", "mobile_no", "membership_start_date", "membership_end_date"],
        order_by="creation desc"
    )
    context.books = frappe.get_all(
        "Books",
        fields=["name", "title", "author", "status", "publisher", "available_copies"],
        order_by="creation desc"
    )


    context.fines = frappe.get_all(
        "Fine",
        fields=["name", "member", "book", "amount", "reason", "date_of_fine", "paid"],
        order_by="creation desc"
    )

    context.transactions = frappe.get_all(
        "Membership Transaction",
        fields=["name", "member", "start_date", "end_date", "paid"],
        order_by="creation desc"
    )

    context.total_members = len(context.members)
    context.total_books = len(context.books)
    context.total_fines = len(context.fines)
    context.total_transactions = len(context.transactions)

    return context
