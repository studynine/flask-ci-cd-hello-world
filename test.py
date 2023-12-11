import unittest
from app import app

class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        client = app.test_client()

        response = client.get('/')
        data = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, Dockerized Flask App!', data)

if __name__ == '__main__':
    unittest.main()
