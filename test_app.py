import unittest
import json
from app import app

class FlaskApiTest(unittest.TestCase):

    def setUp(self):
        
        self.app = app.test_client()

    def test_get_des(self):
        
        response = self.app.get('/desserts')
        self.assertEqual(response.status_code, 200)

        #You can check with this also
        # data = json.loads(response.data)
        # self.assertIsInstance(data, list)
       

    def test_add_dessert(self):
        # Test the POST /desserts endpoint
        data = {'name': 'New Dessert', 'flavour': 'Sweet'}
        response = self.app.post('/desserts', json=data)
        self.assertEqual(response.status_code, 200)

        # response_data = json.loads(response.data)
        # self.assertEqual(response_data['message'], 'dessert added successfully')
       

    def test_update_dessert(self):
        
        sno = 1 
        data = {'name': 'Updated Dessert', 'flavour': 'Tasty'}
        response = self.app.put(f'/desserts/{sno}', json=data)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'], 'dessert updated successfully')
        

    def test_delete_dessert(self):

        sno = 1  
        response = self.app.delete(f'/desserts/{sno}')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'], 'dessert deleted successfully')
       
if __name__ == '__main__':
    unittest.main()
