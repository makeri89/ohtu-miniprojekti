import requests

class AppLibrary:
    def add_weblink_to_database(self, title, url):
        weblink_data = {
            "title": title,
            "url": url
        }
        requests.post("http://localhost:5000/weblinks", data=weblink_data)

    def add_book_to_database(self, title, author, year):
        book_data = {
            "title": title,
            "author": author,
            "year": year
        }
        requests.post("http://localhost:5000/books", data=book_data)

    def add_podcast_to_database(self, title, name, description):
        podcast_data = {
            "title": title,
            "name": name,
            "description": description
        }
        requests.post("http://localhost:5000/podcasts", data=podcast_data)