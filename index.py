from src.app import app
from src.database import db

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0')
