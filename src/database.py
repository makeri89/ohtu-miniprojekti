from flask_sqlalchemy import SQLAlchemy
from app import app
from config import DATABASE_URL

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL or \
    'sqlite://'
    #if no DATABASE_URL given, sqlite database in-memory only
    #if real file is needed for testing, replace above with below
    #'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
