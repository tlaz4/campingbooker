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

    # test user doesnt exist
    def test_get_user_doesnt_exist(self):
        with self.client:
            response = self.client.get('/api/users/1')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    # test bad id provided
    def test_get_user_bad_id(self):
        with self.client:
            response = self.client.get('/api/users/bad')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    # test adding a user
    def test_add_user(self):
        user = {'email': 'tlazaren@ualberta.ca'}

        with self.client:
            response = self.client.post('api/users', 
                data=json.dumps(user),
                content_type='application/json'
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('success', data['status'])
            self.assertIn('tlazaren@ualberta.ca was added', data['message'])

    # add a user with no email
    def test_add_user_no_email(self):
        user = {'phone': '7805546061'}

        with self.client:
            response = self.client.post('api/users',
                data=json.dumps(user),
                content_type='application/json'
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertIn('fail', data['status'])
            self.assertIn('Invalid payload', data['message'])

    # add a user with an incorrectly formatted email
    def test_add_user_bad_email(self):
        user = {'email': 'tlazarenualberta.ca'}

        with self.client:
            response = self.client.post('api/users',
                data=json.dumps(user),
                content_type='application/json'
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertIn('fail', data['status'])
            self.assertIn('Invalid payload', data['message'])

    # test adding a user where the email already exists
    def test_add_user_already_exists(self):
        user = create_user('tlazaren@ualberta.ca')

        with self.client:
            response = self.client.post('api/users',
                data=json.dumps({
                    'email': 'tlazaren@ualberta.ca'
                }),
                content_type='application/json'
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertIn('fail', data['status'])
            self.assertIn('Sorry that user already exists', data['message'])

    # test getting all users
    def test_get_all_users(self):
        user1 = create_user('tlazaren@ualberta.ca')
        user2 = create_user('testemail@test.com')

        with self.client:
            response = self.client.get('api/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertIn('success', data['status'])
            self.assertIn('tlazaren@ualberta.ca', data['data']['users'][0]['email'])
            self.assertIn('testemail@test.com', data['data']['users'][1]['email'])





if __name__ == '__main__':
    unittest.main()