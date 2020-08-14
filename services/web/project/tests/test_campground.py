import json
import unittest

from project.tests.base import BaseTestCase
from project.tests.utils import create_campground

class TestCampgroundService(BaseTestCase):
    """Tests for the campground service"""

    # test getting a campground
    def test_get_campground(self):
        campground = create_campground(
            name='Wabasso Campground',
            park='Jasper National Park'
        )

        with self.client:
            response = self.client.get(f'/api/campgrounds/{campground.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('Wabasso Campground', data['data']['campground_name'])
            self.assertIn('Jasper National Park', data['data']['park'])
            self.assertIn('success', data['status'])

    # test when campground doesnt exist
    def test_get_campground_doesnt_exist(self):
        with self.client:
            response = self.client.get('/api/campgrounds/1')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('Campground does not exist', data['message'])
            self.assertIn('fail', data['status'])

    # test campground with invalid id
    def test_get_campground_bad_id(self):
        with self.client:
            response = self.client.get('api/campgrounds/bad')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('Campground does not exist', data['message'])
            self.assertIn('fail', data['status'])

    # test adding a campground
    def test_add_campground(self):
        campground = {
            'campground_name': 'Wabasso Campground',
            'park': 'Jasper National Park'
        }

        with self.client:
            response = self.client.post('/api/campgrounds',
                data=json.dumps(campground),
                content_type='application/json'
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('success', data['status'])
            self.assertIn('Wabasso Campground was added', data['message'])

    # test adding a campground with no park
    def test_add_campground_no_park(self):
        campground = {
            'campground_name': 'Wabasso Campground',
        }

        with self.client:
            response = self.client.post('/api/campgrounds',
                data=json.dumps(campground),
                content_type='application/json'
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertIn('fail', data['status'])
            self.assertIn('Invalid payload', data['message'])

    # test adding a campground with no name
    def test_add_campground_no_name(self):
        campground = {
            'park': 'Jasper National Park',
        }

        with self.client:
            response = self.client.post('/api/campgrounds',
                data=json.dumps(campground),
                content_type='application/json'
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertIn('fail', data['status'])
            self.assertIn('Invalid payload', data['message'])


    # test adding a campground that already exists
    def test_add_campground_already_exists(self):
        create_campground(
            name='Wabasso Campground',
            park='Jasper National Park'
        )

        campground = {
            'campground_name': 'Wabasso Campground',
            'park': 'Jasper National Park'
        }

        with self.client:
            response = self.client.post('/api/campgrounds',
                data=json.dumps(campground),
                content_type='application/json'
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertIn('fail', data['status'])
            self.assertIn('Sorry that campground already exists', data['message'])


    def test_get_campgrounds(self):
        campground1 = create_campground(
            name='Wapiti Campground',
            park='Jasper National Park'
        )
        campground2 = create_campground(
            name='Wabasso Campground',
            park='Jasper National Park'
        )

        with self.client:
            response = self.client.get('api/campgrounds')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['campgrounds']), 2)
            self.assertEqual(data['data']['campgrounds'][0]['campground_name'], 'Wapiti Campground')
            self.assertEqual(data['data']['campgrounds'][1]['campground_name'], 'Wabasso Campground')
            self.assertIn('success', data['status'])




