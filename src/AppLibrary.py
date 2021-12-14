import requests

class AppLibrary:
    def add_weblink_to_database(self, title, url, comment, course):
        weblink_data = {
            'title': title,
            'url': url,
            'comment': comment,
            'course': course
        }
        requests.post('http://localhost:5000/weblinks', data=weblink_data)

    def add_book_to_database(self, title, author, year, comment, course):
        book_data = {
            'title': title,
            'author': author,
            'year': year,
            'comment': comment,
            'course': course
        }
        requests.post('http://localhost:5000/books', data=book_data)

    def add_podcast_to_database(self, title, name, description, comment, course):
        podcast_data = {
            'title': title,
            'name': name,
            'description': description,
            'comment': comment,
            'course': course
        }
        requests.post('http://localhost:5000/podcasts', data=podcast_data)
        
    def add_course_to_database(self, name):
        course_data = {
            'course_name': name
        }
        requests.post('http://localhost:5000/courses', data=course_data)