from flask import render_template, request, redirect

from app import app
from services.weblink_service import WeblinkService

weblink_service = WeblinkService()

@app.route('/')
def hello_world():
    list_vinks = weblink_service.get_weblinks()
    print(list_vinks)
    return render_template('index.html', weblinks=list_vinks)

@app.route('/weblinks', methods=['GET'])
def weblinks():
    all_weblinks = weblink_service.get_weblinks()
    return str(all_weblinks)

@app.route('/sendvink', methods=['POST'])
def send_vink():
    vink_title = request.form['title']
    vink_url = request.form['url']
    weblink_service.add_weblink(vink_title, vink_url)
    return redirect('/')
