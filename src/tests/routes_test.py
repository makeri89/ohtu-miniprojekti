from app import app
from werkzeug.exceptions import MethodNotAllowed
from unittest import TestCase

class TestRoutes(TestCase):
    test_adapter = app.url_map.bind('')
    
    def test_get_root_returns_index_dictionary(self):
        self.assertEqual(self.test_adapter.match('/'), ('index', {}))

    def test_get_weblinks_returns_weblinks_dictionary(self):
        self.assertEqual(self.test_adapter.match('/weblinks'), ('weblinks', {}))

    def test_post_weblinks_has_post_method(self):
        self.assertTrue(str(self.test_adapter.match('/weblinks', "POST", True)).__contains__('POST'))

    def test_get_podcasts_returns_podcasts_dictionary(self):
        self.assertEqual(self.test_adapter.match('/podcasts'), ('podcasts', {}))

    def test_post_podcasts_has_post_method(self):
        self.assertTrue(str(self.test_adapter.match('/podcasts', "POST", True)).__contains__('POST'))

    def test_get_books_returns_books_dictionary(self):
        self.assertEqual(self.test_adapter.match('/books'), ('books', {}))

    def test_post_books_has_post_method(self):
        self.assertTrue(str(self.test_adapter.match('/books', "POST", True)).__contains__('POST'))

    def test_ping_returns_ping_dictionary(self):
        self.assertEqual(self.test_adapter.match('/ping'), ('ping', {}))

    def test_get_delete_raises_exception(self):
        with self.assertRaises(MethodNotAllowed):
            self.test_adapter.match('/delete')

