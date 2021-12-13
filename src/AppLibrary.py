import requests

class AppLibrary:
    def add_weblink_to_database(self, title, url, comment):
        weblink_data = {
            "title": title,
            "url": url,
            "comment": comment
        }
        requests.post("http://localhost:5000/weblinks", data=weblink_data)

    def add_book_to_database(self, title, author, year, comment):
        book_data = {
            "title": title,
            "author": author,
            "year": year,
            "comment": comment
        }
        requests.post("http://localhost:5000/books", data=book_data)

    def add_podcast_to_database(self, title, name, description, comment):
        podcast_data = {
            "title": title,
            "name": name,
            "description": description,
            "comment": comment
        }
        requests.post("http://localhost:5000/podcasts", data=podcast_data)