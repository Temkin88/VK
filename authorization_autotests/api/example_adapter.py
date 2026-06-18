from api.example import AbstractLoginAdapter, AbstractUserClient
from api.example_http_client import RealHttpClient


class RealAdapter(RealHttpClient):
    __metaclass__ = AbstractLoginAdapter

    def __init__(self):
        super().__init__()

    def real_method(self):
        print("RealAdapter -> real_method")

    def login(self, parent_obj: "AbstractUserClient"):
        print(f"RealAdapter -> login -> parent_obj: {parent_obj}")
        self.real_method()
        parent_obj.real_method()

        parent_obj.aimsid = "TEST_!@#$%^&*()"


class RealAdapterBiz(RealHttpClient):
    __metaclass__ = AbstractLoginAdapter

    def __init__(self):
        super().__init__()

    def auth_types(self, url: str):
        return self.get(url=f"{url}/api/domains/auth-types")

    def login(self, parent_obj: "AbstractUserClient"):
        print(f"RealAdapter -> login -> parent_obj: {parent_obj}")
        self.auth_types()
        parent_obj.real_method()

        parent_obj.aimsid = "TEST_!@#$%^&*()"
