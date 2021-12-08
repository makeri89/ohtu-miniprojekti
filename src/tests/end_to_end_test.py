import requests
import unittest

#placeholder imports before flask_testing is operational
import index
from routes import weblink_service

class TestEndToEnd(unittest.TestCase):
    def setUp(self):
        #creates tables in the database for tests
        index.db.create_all()        
    
    def test_submitted_weblink_is_committed_to_database(self):
        requests.post('http://localhost:5000/weblinks', \
            data={'title': 'end_to_end_testing', 'url': 'http://end.to'})
        results = requests.get('http://localhost:5000/weblinks')
        self.assertTrue(results.text.__contains__('end_to_end_testing'))

    def test_submitted_book_is_committed_to_database(self):
        requests.post('http://localhost:5000/books', \
            data={'title': 'Book Database Commitment', \
                'author': 'Committed Author', 'year': 2021})
        results = requests.get('http://localhost:5000/books')
        self.assertFalse(results.text.__contains__('Book Integrity Commitment'))
        self.assertTrue(results.text.__contains__('Committed Author'))
        self.assertTrue(results.text.__contains__('2021'))
        