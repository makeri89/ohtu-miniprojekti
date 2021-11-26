import unittest

#placeholder import before flask_testing is operational
from routes import weblink_service

class TestWeblink(unittest.TestCase):
    def setUp(self):
        pass

    def test_weblink_has_name_and_url(self):
        weblink_entity = weblink_service.create_weblink_for_testing(title='example', url='http://example.com')
        self.assertEqual(weblink_entity.title, 'example')
        self.assertEqual(weblink_entity.url, 'http://example.com')
        