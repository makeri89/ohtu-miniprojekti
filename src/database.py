from flask_sqlalchemy import SQLAlchemy
from src.app import app
from src.config import DATABASE_URL

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
