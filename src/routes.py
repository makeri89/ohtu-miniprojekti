from flask import render_template, request, redirect

from app import app
from services.weblink_service import WeblinkService

weblink_service = WeblinkService()

@app.route('/', methods=['GET'])
def index():
    weblinks = weblink_service.get_weblinks()
    return render_template('index.html', weblinks=weblinks)

@app.route('/weblinks', methods=['GET', 'POST'])
def weblinks():
    if request.method == 'GET':
        weblinks = weblink_service.get_weblinks()
        return render_template('index.html', weblinks=weblinks)
    if request.method == 'POST':
        weblink_title = request.form['title']
        weblink_url = request.form['url']
        weblink_service.add_weblink(weblink_title, weblink_url)
        return redirect('/weblinks')
    
@app.route('/podcasts', methods=['GET', 'POST'])
def podcasts():
    if request.method == 'GET':
        podcasts = None
        return render_template('index.html', podcasts=podcasts)
    
@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        books = None
        return render_template('index.html', books=books)
