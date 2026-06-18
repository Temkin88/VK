from api.example import AbstractUserClient, AbstractLoginAdapter
from api.example_http_client import RealHttpClient


class RealUserClient(RealHttpClient):
    __metaclass__ = AbstractUserClient

    def __init__(self, login_adapter: "AbstractLoginAdapter", **kwargs) -> None:
        super().__init__()
        self.login_adapter = login_adapter
        aimsid = None

    def real_method(self):
        print("RealUserClient -> real_method")

    def login(self):
        print("RealUserClient -> login -> self.login_adapter.login()")
        self.login_adapter.login(self)

        print(f"RealUserClient -> login -> {aimsid}")
