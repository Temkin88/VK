from abc import ABC, abstractmethod
from typing import Literal

import requests

class AbstractHttpClient(ABC):

    @abstractmethod
    def __init__(self, http_session: requests.Session, **kwargs) -> None:
        self.http_session = http_session
        self.http_session.hooks = {
            "response": [self.check_response]
        }

    @abstractmethod
    def check_response(self, response: requests.Response, *args, **kwargs): ...

    @abstractmethod
    def request(self, method: Literal["GET", "POST"], url: str, **kwargs) -> requests.Response: ...

    @abstractmethod
    def get(self, url: str, **kwargs) -> requests.Response: ...

    @abstractmethod
    def post(self, url: str, **kwargs) -> requests.Response: ...

    @abstractmethod
    def delete(self, url: str, **kwargs) -> requests.Response: ...


class AbstractLoginAdapter(ABC):

    @abstractmethod
    def login(self, parent_obj: "AbstractUserClient") -> None: ...


class AbstractUserClient(ABC):

    @abstractmethod
    def __init__(self, http_session: requests.Session, login_adapter: "AbstractLoginAdapter", **kwargs) -> None:
        self.http_session = http_session
        self.login_adapter = login_adapter

    @abstractmethod
    def login(self):
        self.login_adapter.login(self)
