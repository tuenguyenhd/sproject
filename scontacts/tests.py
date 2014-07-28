from unittest import TestCase
from scontacts.models import Contact

class ContactTests(TestCase):
    """Contact model tests."""

    def test_str(self):
        contact = Contact(name='Trang',password='Ban Anh Thang')
        self.assertEqual(str(contact),'Trang Ban Anh Thang')