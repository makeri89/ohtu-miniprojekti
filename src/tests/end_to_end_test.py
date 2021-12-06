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
        results = requests.get('http://localhost:5000/')
        self.assertTrue(results.text.__contains__('end_to_end_testing'))
        