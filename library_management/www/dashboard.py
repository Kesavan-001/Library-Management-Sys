import frappe

def get_context(getdata):
    getdata.members = frappe.get_all(
        "Library Member",
        fields=["name", "name1", "email", "mobile_no", "membership_start_date", "membership_end_date"],
        order_by="creation desc"
    )
    getdata.books = frappe.get_all(
        "Books",
        fields=["name", "title", "author", "status", "publisher", "available_copies", "cover_image"],
        order_by="creation desc"
    )


    getdata.fines = frappe.get_all(
        "Fine",
        fields=["name", "member", "book", "amount", "reason", "date_of_fine", "paid"],
        order_by="creation desc"
    )

    getdata.transactions = frappe.get_all(
        "Membership Transaction",
        fields=["name", "member", "start_date", "end_date", "paid"],
        order_by="creation desc"
    )

    getdata.bookissue = frappe.get_all(
        "Book Issue",
        fields=["name","member","custom_name","book","issue_date"],
        order_by="creation desc"
    )


    getdata.total_members = len(getdata.members)
    getdata.total_books = len(getdata.books)
    getdata.total_fines = len(getdata.fines)
    getdata.total_transactions = len(getdata.transactions)
    getdata.book_issue = len(getdata.bookissue)

    return getdata
