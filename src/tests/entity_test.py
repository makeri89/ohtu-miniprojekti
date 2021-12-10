from database import db
from flask import Flask
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
from entities.weblink import Weblink
from entities.book import Book
from entities.podcast import Podcast
from services.weblink_service import WeblinkService

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
        weblink_entity = Weblink('Newly Created Weblink', 'http://example.com')
        self.assertEqual(weblink_entity.title, 'Newly Created Weblink')
        self.assertEqual(weblink_entity.url, 'http://example.com')

    def test_weblink_holds_integrity_in_and_out_of_database(self):
        db.session.add(Weblink('Weblink For Integrity Test', 'http://example.com'))
        db.session.commit()
        ##change below to fetch only specific weblink
        all_weblinks = Weblink.query.all()
        self.assertEqual(all_weblinks[-1].title, 'Weblink For Integrity Test')
        self.assertEqual(all_weblinks[-1].url, 'http://example.com')

    def test_delete_weblink_from_database(self):
        weblink = Weblink('Weblink For Integrity Test', 'http://example.com')
        db.session.add(weblink)
        db.session.commit()
        db.session.delete(weblink)
        db.session.commit()
        self.assertIsNone(Weblink.query.filter_by(title='Weblink For Integrity Test').first())    
        
    def test_book_has_name_and_author(self):
        book_entity = Book('Book Title For Testing', 'Book A. Uthor', 2021)
        self.assertEqual(book_entity.title, 'Book Title For Testing')
        self.assertEqual(book_entity.author, 'Book A. Uthor')
        self.assertNotEqual(book_entity.year, 2020)

    def test_book_holds_integrity_in_and_out_of_database(self):
        db.session.add(Book('Book For Integrity Test', 'Named Author', 2021))
        db.session.commit()
        ##change below to fetch only specific book
        all_books = Book.query.all()
        self.assertEqual(all_books[-1].title, 'Book For Integrity Test')
        self.assertNotEqual(all_books[-1].author, 'Someone Else')
        self.assertEqual(all_books[-1].year, 2021)
    
    def test_podcast_has_title_name_and_description(self):
        podcast_entity = Podcast('Podcast Title', 'Podcast Name', 'Podcast Description')
        self.assertEqual(podcast_entity.title, 'Podcast Title')
        self.assertEqual(podcast_entity.name, 'Podcast Name')
        self.assertNotEqual(podcast_entity.description, 'Wrong Description')

    def test_podcast_holds_integrity_in_and_out_of_database(self):
        db.session.add(Podcast('Podcast For Integrity Test', 'Podcast Name', 'Podcast Description'))
        db.session.commit()
        all_podcasts = Podcast.query.all()
        self.assertEqual(all_podcasts[-1].title, 'Podcast For Integrity Test')
        self.assertNotEqual(all_podcasts[-1].name, 'Wrong name')
        self.assertEqual(all_podcasts[-1].description, 'Podcast Description')
   

