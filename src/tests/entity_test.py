import unittest
from entity import Weblink

class TestWeblink(unittest.TestCase):
    def setUp(self):
        pass

    def test_weblink_has_name_and_url(self):
        weblink_entity = Weblink('example', 'http://example.com')
        self.assertEqual(weblink_entity.get_title, 'example')
        self.assertEqual(weblink_entity.get_url, 'http://example.com')