from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import unittest
from entity import Weblink

from flask_testing import TestCase

#from app import app
#from entity import db

class TestWeblink(unittest.TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True
    db = SQLAlchemy()    
    def create_app(self):
        app = Flask(__name__)

        self.db.init_app(app)
        app.app_context().push()
        return app

    def setUp(self):
        self.db = SQLAlchemy(self.create_app())
        self.db.create_all()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_weblink_has_name_and_url(self):
        weblink_entity = Weblink(title='example', url='http://example.com')
        self.assertEqual(weblink_entity.title, 'example')
        self.assertEqual(weblink_entity.url, 'http://example.com')
        