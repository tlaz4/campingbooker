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


