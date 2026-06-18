import requests

from api.example import AbstractUserClient


class RealHttpClient:
    __metaclass__ = AbstractUserClient

    def __init__(self):
        self.http_session = requests.Session()
        self.http_session.hooks = {
            "response": [self.check_response]
        }

    def check_response(self, response, *args, **kwargs):
        print(response)

    def request(self, method, url, **kwargs):
        return self.http_session.request(method, url, **kwargs)

    def get(self, url, **kwargs):
        return self.request("GET", url, **kwargs)

    def post(self, url, **kwargs):
        return self.request("POST", url, **kwargs)

    def delete(self, url, **kwargs):
        return self.request("DELETE", url, **kwargs)
