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