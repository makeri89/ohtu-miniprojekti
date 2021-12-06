import requests

class AppLibrary:
    def add_weblink_to_database(self, title, url):
        weblink_data = {
            "title": title,
            "url": url
        }
        requests.post("http://localhost:5000/weblinks", data=weblink_data)
