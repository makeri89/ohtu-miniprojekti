from database import db
from flask import Flask
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import InvalidRequestError
from entities.weblink import Weblink
from entities.book import Book
from entities.podcast import Podcast

class TestEntities(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['TESTING'] = True
        
        #SQLAlchemy has to be initialized as below,
        #even though we utilize DB as set in database module
        #(from database import db)
        SQLAlchemy(app)
        
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_weblink_has_name_and_url(self):
        weblink_entity = Weblink('Newly Created Weblink', 'http://example.com', 'WebLink Comment')
        self.assertEqual(weblink_entity.title, 'Newly Created Weblink')
        self.assertEqual(weblink_entity.url, 'http://example.com')

    def test_weblink_holds_integrity_in_and_out_of_database(self):
        db.session.add(Weblink('Weblink For Integrity Test', 'http://example.com', 'WebLink Comment'))
        db.session.commit()
        weblink = Weblink.query.filter_by(title='Weblink For Integrity Test').first()
        self.assertEqual(weblink.title, 'Weblink For Integrity Test')
        self.assertEqual(weblink.url, 'http://example.com')

    def test_delete_weblink_from_database(self):
        weblink = Weblink('Weblink For Delete Test', 'http://example.com', 'Weblink comment')
        db.session.add(weblink)
        db.session.commit()
        db.session.delete(weblink)
        db.session.commit()
        self.assertIsNone(Weblink.query.filter_by(title='Weblink For Delete Test').first())    
        
    def test_book_has_name_and_author(self):
        book_entity = Book('Book Title For Testing', 'Book A. Uthor', 2021, 'Book Comment')
        self.assertEqual(book_entity.title, 'Book Title For Testing')
        self.assertEqual(book_entity.author, 'Book A. Uthor')
        self.assertNotEqual(book_entity.year, 2020)

    def test_book_holds_integrity_in_and_out_of_database(self):
        db.session.add(Book('Book For Integrity Test', 'Named Author', 2021, 'Book Comment'))
        db.session.commit()
        book = Book.query.filter_by(title='Book For Integrity Test').first()
        self.assertEqual(book.title, 'Book For Integrity Test')
        self.assertNotEqual(book.author, 'Someone Else')
        self.assertEqual(book.year, 2021)

    def test_delete_book_from_database(self):
        book = Book('Book For Integrity Test', 'Named Author', 2021, 'Book Comment')
        db.session.add(book)
        db.session.commit()
        db.session.delete(book)
        db.session.commit()
        self.assertIsNone(Book.query.filter_by(title='Book For Integrity Test').first())    
    
    def test_podcast_has_title_name_and_description(self):
        podcast_entity = Podcast('Podcast Title', 'Podcast Name', 'Podcast Description', 'Podcast Comment')
        self.assertEqual(podcast_entity.title, 'Podcast Title')
        self.assertEqual(podcast_entity.name, 'Podcast Name')
        self.assertNotEqual(podcast_entity.description, 'Wrong Description')

    def test_podcast_holds_integrity_in_and_out_of_database(self):
        db.session.add(Podcast('Podcast For Integrity Test', 'Podcast Name', 'Podcast Description', 'Podcast Comment'))
        db.session.commit()
        podcast = Podcast.query.filter_by(title='Podcast For Integrity Test').first()
        self.assertEqual(podcast.title, 'Podcast For Integrity Test')
        self.assertNotEqual(podcast.name, 'Wrong name')
        self.assertEqual(podcast.description, 'Podcast Description')

    def test_delete_podcast_from_database(self):
        podcast = Podcast('Podcast Created For Delete Test', 'Podcast Author', 'Podcast To Be Deleted', 'Podcast Comment')
        db.session.add(podcast)
        self.assertIsNone(podcast.id)
        db.session.commit()
        self.assertIsNotNone(podcast.id)
        db.session.delete(podcast)
        db.session.commit()
        self.assertIsNone(Podcast.query.filter_by(title='Podcast Created For Delete Test').first())
   
    def test_attempt_delete_nonexistent_podcast_raises_exception(self):
        podcast = Podcast('Podcast Not Committed To DB', 'Podcast Author', 'Podcast To Raise Expcetion')
        with self.assertRaises(InvalidRequestError):
            db.session.delete(podcast)
