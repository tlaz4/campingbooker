import json
import unittest

from project.tests.base import BaseTestCase
from project.tests.utils import create_user

class TestUserService(BaseTestCase):
    """Tests for the users api"""

    def test_users(self):
        response = self.client.get('/api/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    # test getting a single user by id
    def test_get_user(self):
        user = create_user(email='tlazaren@ualberta.ca')

        with self.client:
            response = self.client.get(f'/api/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('tlazaren@ualberta.ca', data['data']['email'])
            self.assertIn('success', data['status'])



if __name__ == '__main__':
    unittest.main()