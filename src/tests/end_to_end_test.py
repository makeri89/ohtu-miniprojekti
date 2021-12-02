import requests
import unittest

#placeholder import before flask_testing is operational
from routes import weblink_service

class TestEndToEnd(unittest.TestCase):
    def test_submitted_weblink_is_committed_to_database(self):
        requests.post('http://localhost:5000/sendvink', \
            data={'title': 'end_to_end_testing', 'url': 'http://end.to'})
        results = requests.get('http://localhost:5000/weblinks')
        self.assertTrue(results.text.__contains__('end_to_end_testing'))
        