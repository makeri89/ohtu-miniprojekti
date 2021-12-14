from app import app
from database import db
from config import PORT, HOST

port = PORT or 5000

@app.before_first_request
def setup():
    db.create_all()

if __name__ == '__main__':
    db.create_all()
    app.run(port=port, host=HOST)
