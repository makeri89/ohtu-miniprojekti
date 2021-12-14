from werkzeug.wrappers import response
from services.book_service import BookService
from services.podcast_service import PodcastService
from services.weblink_service import WeblinkService
from services.course_service import CourseService
from unittest import TestCase

class TestIntegrity(TestCase):
    book_service = BookService()
    podcast_service = PodcastService()
    weblink_service = WeblinkService()
    course_service = CourseService()
    
    def setUp(self):
        self.course_service.add_course('Testing 101')
    
    def test_added_course_is_committed_to_database(self):
        self.course_service.add_course('Testing 205')
        response = self.course_service.get_courses()
        self.assertEqual(response[-1].name, 'Testing 205')
        
    def test_deleted_course_gone_from_database(self):
        id = self.weblink_service.get_weblinks()[-1].id
        self.course_service.delete_course(id)
        self.assertEqual(self.course_service.get_course_by_id(id), None)

    def test_added_weblink_is_committed_to_database(self):
        self.weblink_service.add_weblink('Integrity Weblink', 'http://in.te', 'No comment', 'Testing 101')
        response = self.weblink_service.get_weblinks()
        self.assertEqual(response[-1].title, 'Integrity Weblink')

    def test_deleted_weblink_is_gone_from_database(self):
        id = self.weblink_service.get_weblinks()[-1].id
        self.weblink_service.delete_weblink(id)
        self.assertEqual(self.weblink_service.get_weblink_by_id(id), None)

    def test_added_book_is_committed_to_database(self):
        print('XXXXX')
        self.book_service.add_book('Integrity Book', 'Author', 2021, 'No comment', 'Testing 101')
        response = self.book_service.get_books()
        print('XXXXX', response)
        self.assertEqual(response[-1].title, 'Integrity Book')

    def test_deleted_book_is_gone_from_database(self):
        id = self.book_service.get_books()[-1].id
        self.book_service.delete_book(id)
        self.assertEqual(self.book_service.get_book_by_id(id), None)

    def test_added_podcast_is_committed_to_database(self):
        self.podcast_service.add_podcast('Integrity Podcast', 'Author Name', 'Description', 'No comment', 'Testing 101')
        response = self.podcast_service.get_podcasts()
        self.assertEqual(response[-1].title, 'Integrity Podcast')

    def test_deleted_podcast_is_gone_from_database(self):
        id = self.podcast_service.get_podcasts()[-1].id
        self.podcast_service.delete_podcast(id)
        self.assertEqual(self.podcast_service.get_podcast_by_id(id), None)
