import unittest
import app

class testApp(unittest.TestCase):

	def test_add_product(self):

		result=app.test_client(self)
		response=result.get('/product')
		statuscode=response.status_code
		self.assertEqual(statuscode, 200)


if __name__=="__main__":
	unittest.main()