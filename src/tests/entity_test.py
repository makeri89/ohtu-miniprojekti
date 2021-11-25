import unittest
from entity import Weblink

class TestWeblink(unittest.TestCase):
    def setUp(self):
        pass

    def test_weblink_has_name_and_url(self):
        weblink_entity = Weblink(title='example', url='http://example.com')
        self.assertEqual(weblink_entity.title, 'example')
        self.assertEqual(weblink_entity.url, 'http://example.com')
        