import unittest

#placeholder imports before flask_testing is operational
import index
from routes import weblink_service, book_service

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
        
    def test_book_has_name_and_author(self):
        book_entity = book_service.create_book_for_testing(title='Book Title For Testing', author='Book A. Uthor', year=2021)
        self.assertEqual(book_entity.title, 'Book Title For Testing')
        self.assertEqual(book_entity.author, 'Book A. Uthor')
        self.assertNotEqual(book_entity.year, 2020)

    def test_book_holds_integrity_in_and_out_of_database(self):
        book_service.add_book('Book Integrity Test', 'Named Author', 2021)
        #change below to fetch only specific book
        all_books = book_service.get_books()
        self.assertEqual(all_books[-1].title, 'Book Integrity Test')
        self.assertNotEqual(all_books[-1].author, 'Someone Else')
        self.assertEqual(all_books[-1].year, 2021)