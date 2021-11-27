from flask import render_template

from app import app
from services.weblink_service import weblink_service

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/weblinks', methods=['GET'])
def weblinks():
    all_weblinks = weblink_service.get_weblinks()
    return str(all_weblinks)
