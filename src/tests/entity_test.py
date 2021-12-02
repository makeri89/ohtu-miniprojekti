import index
import unittest

#placeholder import before flask_testing is operational
from routes import weblink_service

class TestWeblink(unittest.TestCase):
    def setUp(self):
        #creates tables in the database for tests
        index.db.create_all()        

    def test_weblink_has_name_and_url(self):
        weblink_entity = weblink_service.create_weblink_for_testing(title='example', url='http://example.com')
        self.assertEqual(weblink_entity.title, 'example')
        self.assertEqual(weblink_entity.url, 'http://example.com')

    def test_weblink_holds_integrity_in_and_out_of_database(self):
        weblink_service.add_weblink('example1', 'http://example1.com')
        #change below to fetch only specific weblink
        all_weblinks = weblink_service.get_weblinks()
        self.assertEqual(all_weblinks[-1].title, 'example1')
        self.assertEqual(all_weblinks[-1].url, 'http://example1.com')
        