from flask import render_template, request, redirect

from app import app
from services.weblink_service import WeblinkService
from services.book_service import BookService
from services.podcast_service import PodcastService
from services.course_service import CourseService

weblink_service = WeblinkService()
book_service = BookService()
podcast_service = PodcastService()
course_service = CourseService()

@app.route('/', methods=['GET'])
def index():
    all_weblinks = weblink_service.get_weblinks()
    all_books = book_service.get_books()
    all_podcasts =podcast_service.get_podcasts()
    return render_template('index.html', weblinks=all_weblinks,
                           books=all_books,podcasts=all_podcasts)

@app.route('/weblinks', methods=['GET', 'POST'])
def weblinks():
    if request.method == 'GET':
        all_weblinks = weblink_service.get_weblinks()
        all_courses = course_service.get_courses()
        return render_template('vinks.html',
                               weblinks=all_weblinks,
                               courses=all_courses)
    if request.method == 'POST':
        weblink_title = request.form['title']
        weblink_url = request.form['url']
        weblink_comment = request.form['comment']
        weblink_course = request.form['course']
        weblink_service.add_weblink(weblink_title, weblink_url, \
            weblink_comment, weblink_course)
        return redirect('/weblinks')

@app.route('/podcasts', methods=['GET', 'POST'])
def podcasts():
    if request.method == 'GET':
        all_podcasts = podcast_service.get_podcasts()
        all_courses = course_service.get_courses()
        return render_template('vinks.html',
                               podcasts=all_podcasts,
                               courses=all_courses)
    if request.method == 'POST':
        podcast_title = request.form['title']
        podcast_name = request.form['name']
        podcast_description = request.form['description']
        podcast_comment = request.form['comment']
        podcast_course = request.form['course']
        podcast_service.add_podcast(podcast_title, podcast_name, \
             podcast_description, podcast_comment, podcast_course)
        return redirect('/podcasts')

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        all_books = book_service.get_books()
        all_courses = course_service.get_courses()
        return render_template('vinks.html',
                               books=all_books,
                               courses=all_courses)
    if request.method == 'POST':
        book_title = request.form['title']
        book_author = request.form['author']
        book_year = request.form['year']
        book_comment = request.form['comment']
        book_course = request.form['course']
        book_service.add_book(book_title, book_author, book_year,
                              book_comment, book_course)
        return redirect('/books')

@app.route('/courses', methods=['GET', 'POST'])
def courses():
    if request.method == 'GET':
        all_courses = course_service.get_courses()
        return render_template('courses.html', courses=all_courses)
    if request.method == 'POST':
        course_name = request.form['course_name']
        course_service.add_course(course_name)
        return redirect('/courses')

@app.route('/delete', methods=['POST'])
def delete():
    if 'weblink.id' in request.form:
        deleted_weblink = request.form['weblink.id']
        weblink_service.delete_weblink(deleted_weblink)
        return redirect('/weblinks')
    if 'podcast.id' in request.form:
        deleted_podcast = request.form['podcast.id']
        podcast_service.delete_podcast(deleted_podcast)
        return redirect('/podcasts')
    if 'book.id' in request.form:
        deleted_book = request.form['book.id']
        book_service.delete_book(deleted_book)
        return redirect('/books')
    if 'course.id' in request.form:
        course_to_delete = request.form['course.id']
        course_service.delete_course(course_to_delete)
        return redirect('/courses')

@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'
