from flask import render_template, request

from app import app
from services.weblink_service import WeblinkService

weblink_service = WeblinkService()

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/weblinks', methods=['GET'])
def weblinks():
    all_weblinks = weblink_service.get_weblinks()
    return str(all_weblinks)

@app.route('/addlink', methods=['GET', 'POST'])
def addLink():
    if request.method == 'POST':
        title = request.form['title']
        url = request.form['url']
        weblink_service.add_weblink(title, url)  
    
    return render_template("addlink.html")