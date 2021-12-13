#import required for flask/unittest integration
from app import app

from entities.podcast import Podcast
from entities.book import Book
from entities.weblink import Weblink
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
        
    def test_submitted_podcast_is_committed_to_database(self):
        requests.post(f'http://localhost:{PORT}/podcasts', \
            data={'title': 'Commit Podcast to Dabase', \
                'name': 'Database Podcast',  \
                'description': 'Podcast about committing data into a database'})
        results = requests.get(f'http://localhost:{PORT}/podcasts')
        self.assertFalse(results.text.__contains__('Podcast title'))
        self.assertTrue(results.text.__contains__('Database Podcast'))
        self.assertTrue(results.text.__contains__('Podcast about committing data into a database'))

    def test_deleted_podcast_is_removed_from_database(self):
        requests.post(f'http://localhost:{PORT}/podcasts', \
            data={'title': 'End-to-end Podcast To Be Deleted', \
                'name': 'Deleted Author', 'description': 'This Podcase Is Soon Gone'})
        results = requests.get(f'http://localhost:{PORT}/podcasts')
        self.assertTrue(results.text.__contains__('End-to-end Podcast To Be Deleted'))
        #instead of parsing HTML for podcast.id
        #below I simply fetch the latest podcast.id from db directly
        podcast_id = Podcast.query.all()[-1].id
        requests.post(f'http://localhost:{PORT}/delete', \
            data={'podcast.id': str(podcast_id)})
        results = requests.get(f'http://localhost:{PORT}/podcasts')
        self.assertFalse(results.text.__contains__('End-to-end Podcast To Be Deleted'))

    def test_deleted_book_is_removed_from_database(self):
        requests.post(f'http://localhost:{PORT}/books', \
            data={'title': 'Book Database Commitment', \
                'author': 'Committed Author', 'year': 2021})
        results = requests.get(f'http://localhost:{PORT}/books')
        #instead of parsing HTML for podcast.id
        #below I simply fetch the latest podcast.id from db directly
        book_id = Book.query.all()[-1].id
        requests.post(f'http://localhost:{PORT}/delete', \
            data={'book.id': str(book_id)})
        results = requests.get(f'http://localhost:{PORT}/books')
        self.assertFalse(results.text.__contains__('End-to-end Book To Be Deleted'))    
        