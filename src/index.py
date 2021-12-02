import app
from database import db

if __name__ == '__main__':
    db.create_all()
    app.app.run(host='0.0.0.0')
