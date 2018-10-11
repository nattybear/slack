from urllib.request import urlopen, Request
from json import dumps

class Webhook:
    headers = {"Content-type": "application/json"}

    def __init__(self, url):
        self.url = url

    def set_data(self, dictionary):
        json = dumps(dictionary)
        self.data = json.encode("utf-8")

    def send(self):
        request = Request(self.url, data=self.data, headers=self.headers)
        response = urlopen(request)
        response.close()

    def send_text(self, text):
        dictionary = {"text" : text}
        self.set_data(dictionary)
        self.send()

    def send_attachment(self, title, link):
        sub_dictionary = {"title" : title, "title_link" : link}
        dictionary = {"attachments" : [sub_dictionary]}
        self.set_data(dictionary)
        self.send()
