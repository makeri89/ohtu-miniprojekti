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
    
    def test_added_course_is_committed_to_database(self):
        self.course_service.add_course('Testing 205')
        response = self.course_service.get_courses()
        self.assertEqual(response[-1].name, 'Testing 205')

    def test_added_weblink_is_committed_to_database(self):
        self.weblink_service.add_weblink('Integrity Weblink', 'http://in.te', 'No comment', 'Testing 205')
        response = self.weblink_service.get_weblinks()
        self.assertEqual(response[-1].title, 'Integrity Weblink')

    def test_deleted_weblink_is_gone_from_database(self):
        id = self.weblink_service.get_weblinks()[-1].id
        self.weblink_service.delete_weblink(id)
        self.assertNotEqual(self.weblink_service.get_weblinks()[-1].id, id)

    def test_added_book_is_committed_to_database(self):
        self.book_service.add_book('Integrity Book', 'Author', 2021, 'No comment')
        response = self.book_service.get_books()
        self.assertEqual(response[-1].title, 'Integrity Book')

    def test_deleted_book_is_gone_from_database(self):
        id = self.book_service.get_books()[-1].id
        self.book_service.delete_book(id)
        self.assertNotEqual(self.book_service.get_books()[-1].id, id)

    def test_added_podcast_is_committed_to_database(self):
        self.podcast_service.add_podcast('Integrity Podcast', 'Author Name', 'Description', 'No comment')
        response = self.podcast_service.get_podcasts()
        self.assertEqual(response[-1].title, 'Integrity Podcast')

    def test_deleted_podcast_is_gone_from_database(self):
        id = self.podcast_service.get_podcasts()[-1].id
        self.podcast_service.delete_podcast(id)
        self.assertNotEqual(self.podcast_service.get_podcasts()[-1].id, id)
