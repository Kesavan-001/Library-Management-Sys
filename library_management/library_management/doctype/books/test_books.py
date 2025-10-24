# Copyright (c) 2025, Kesavan and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestBooks(FrappeTestCase):
	
	def test_book_creation(self):
		book = frappe.get_doc({
			"doctype":"Books",
			"title":"Python",
			"author":"Kesavan",
			"isbn":"12345678",
			"publisher":"sys"
		})
		book.insert()

		self.assertEqual(book.title,"Python")
		self.assertEqual(book.author,"Kesavan")
		self.assertEqual(book.isbn,"12345678")
		self.assertEqual(book.publisher,"sys")
		
	def test_book_availability(self):
		book = frappe.get_doc({
			"doctype":"Books",
			"title":"Django",
			"author":"Raju",
			"isbn":"87654321",
			"publisher":"abc",
			"total_copies":5,
			"available_copies":5
		})
		book.insert()

		self.assertEqual(book.available_copies,5)
		self.assertEqual(book.total_copies,5)