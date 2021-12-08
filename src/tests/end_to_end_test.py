#import required for flask/unittest integration
from app import app

import requests
from unittest import TestCase

PORT = 5000

class TestEndToEnd(TestCase):
    def test_submitted_weblink_is_committed_to_database(self):
        requests.post(f'http://localhost:{PORT}/weblinks', \
            data={'title': 'End to End Testing for Weblinks', 'url': 'http://end.to'})
        results = requests.get(f'http://localhost:{PORT}/weblinks')
        self.assertTrue(results.text.__contains__('End to End Testing for Weblinks'))

    def test_submitted_book_is_committed_to_database(self):
        requests.post(f'http://localhost:{PORT}/books', \
            data={'title': 'Book Database Commitment', \
                'author': 'Committed Author', 'year': 2021})
        results = requests.get(f'http://localhost:{PORT}/books')
        self.assertFalse(results.text.__contains__('Book Integrity Commitment'))
        self.assertTrue(results.text.__contains__('Committed Author'))
        self.assertTrue(results.text.__contains__('2021'))
        