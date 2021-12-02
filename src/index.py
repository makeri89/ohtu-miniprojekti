from app import app
from database import db
from config import PORT, HOST

port = PORT or 33507

if __name__ == '__main__':
    db.create_all()
    app.run(port=port, host=HOST)
