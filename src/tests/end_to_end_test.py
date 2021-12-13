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
            data={'title': 'End to End Testing for Weblinks', 'url': 'http://end.to', \
                'comment': 'Weblink Comment'})
        results = requests.get(f'http://localhost:{PORT}/weblinks')
        self.assertTrue(results.text.__contains__('End to End Testing for Weblinks'))
        self.assertTrue(results.text.__contains__('Weblink Comment'))

    def test_submitted_book_is_committed_to_database(self):
        requests.post(f'http://localhost:{PORT}/books', \
            data={'title': 'Book Database Commitment', \
                'author': 'Committed Author', 'year': 2021, 'comment': 'Book Comment'})
        results = requests.get(f'http://localhost:{PORT}/books')
        self.assertFalse(results.text.__contains__('Book Integrity Commitment'))
        self.assertTrue(results.text.__contains__('Committed Author'))
        self.assertTrue(results.text.__contains__('2021'))
        self.assertTrue(results.text.__contains__('Book Comment'))
        
    def test_submitted_podcast_is_committed_to_database(self):
        requests.post(f'http://localhost:{PORT}/podcasts', \
            data={'title': 'Commit Podcast to Dabase', \
                'name': 'Database Podcast',  \
                'description': 'Podcast about committing data into a database',  \
                'comment': 'Podcast Comment'})
        results = requests.get(f'http://localhost:{PORT}/podcasts')
        self.assertFalse(results.text.__contains__('Podcast title'))
        self.assertTrue(results.text.__contains__('Database Podcast'))
        self.assertTrue(results.text.__contains__('Podcast about committing data into a database'))
        self.assertTrue(results.text.__contains__('Podcast Comment'))

    def test_deleted_podcast_is_removed_from_database(self):
        requests.post(f'http://localhost:{PORT}/podcasts', \
            data={'title': 'End-to-end Podcast To Be Deleted', \
                'name': 'Deleted Author', 'description': 'This Podcase Is Soon Gone', \
                'comment': 'Deleted Comment'})
        results = requests.get(f'http://localhost:{PORT}/podcasts')
        self.assertTrue(results.text.__contains__('End-to-end Podcast To Be Deleted'))
        self.assertTrue(results.text.__contains__('Deleted Comment'))
        #instead of parsing HTML for podcast.id
        #below I simply fetch the latest podcast.id from db directly
        podcast_id = Podcast.query.all()[-1].id
        requests.post(f'http://localhost:{PORT}/delete', \
            data={'podcast.id': str(podcast_id)})
        results = requests.get(f'http://localhost:{PORT}/podcasts')
        self.assertFalse(results.text.__contains__('End-to-end Podcast To Be Deleted'))
        self.assertFalse(results.text.__contains__('Deleted Commment'))

    def test_deleted_book_is_removed_from_database(self):
        requests.post(f'http://localhost:{PORT}/books', \
            data={'title': 'Book Database Commitment', \
                'author': 'Committed Author', 'year': 2021, 'comment': 'Deleted Book Comment'})
        results = requests.get(f'http://localhost:{PORT}/books')
        #instead of parsing HTML for podcast.id
        #below I simply fetch the latest podcast.id from db directly
        book_id = Book.query.all()[-1].id
        requests.post(f'http://localhost:{PORT}/delete', \
            data={'book.id': str(book_id)})
        results = requests.get(f'http://localhost:{PORT}/books')
        self.assertFalse(results.text.__contains__('End-to-end Book To Be Deleted'))    
        self.assertFalse(results.text.__contains__('Deleted Book Comment'))    
        