import unittest
import json
from app import app

class FlaskApiTest(unittest.TestCase):

    def setUp(self):
        
        self.app = app.test_client()

    def test_get_des(self):
        # Test the GET /desserts endpoint
        response = self.app.get('/desserts')
        self.assertEqual(response.status_code, 200)
        # data = json.loads(response.data)
        # self.assertIsInstance(data, list)
        # Add more assertions to validate the response data

    def test_add_dessert(self):
        # Test the POST /desserts endpoint
        data = {'name': 'New Dessert', 'flavour': 'Sweet'}
        response = self.app.post('/desserts', json=data)
        self.assertEqual(response.status_code, 200)
        # response_data = json.loads(response.data)
        # self.assertEqual(response_data['message'], 'dessert added successfully')
        # Add more assertions to check if the user was actually added in the database

    def test_update_dessert(self):
        # Test the PUT /desserts/<sno> endpoint
        sno = 1  # Assuming there is a dessert with sno = 1 in the database
        data = {'name': 'Updated Dessert', 'flavour': 'Tasty'}
        response = self.app.put(f'/desserts/{sno}', json=data)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'], 'dessert updated successfully')
        # Add more assertions to check if the dessert was actually updated in the database

    def test_delete_dessert(self):
        # Test the DELETE /desserts/<sno> endpoint
        sno = 1  # Assuming there is a dessert with sno = 1 in the database
        response = self.app.delete(f'/desserts/{sno}')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'], 'dessert deleted successfully')
        # Add more assertions to check if the dessert was actually deleted from the database

if __name__ == '__main__':
    unittest.main()
