import unittest
import urllib.request
import urllib.parse
import json
import make_requests3

class TestRequests(unittest.TestCase):

	def test_check_int(self):
		self.assertTrue(make_requests3.check_int(1000))
		self.assertFalse(make_requests3.check_int(1000.0))
		self.assertFalse(make_requests3.check_int('1000'))

	def test_check_str(self):
		self.assertTrue(make_requests3.check_int(1000))
		self.assertFalse(make_requests3.check_int(1000.0))
		self.assertFalse(make_requests3.check_int('1000'))

	def check_page_end(self):
		self.assertEqual(make_requests3.check_page_end(0,1000,4000),4)
		self.assertEqual(make_requests3.check_page_end(1,1000,4000),3)


if __name__ == '__main__':
	unittest.main()

