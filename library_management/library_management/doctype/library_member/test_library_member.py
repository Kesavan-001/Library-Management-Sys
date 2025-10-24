import frappe
from frappe.tests.utils import FrappeTestCase
from faker import Faker

fake = Faker('en_IN')
class TestLibraryMember(FrappeTestCase):

	def test_member_creation(self):
		mobile = "+91" + fake.numerify(text ="9#########")
		email = fake.email()
		member = frappe.get_doc({
			"doctype": "Library Member",
			"email": email,
			"mobile_no": mobile
		}).insert()

		self.assertEqual(member.email, email)
		self.assertEqual(member.mobile_no, mobile)
