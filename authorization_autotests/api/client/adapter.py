from api.ABC.abstract_client import AbstractLoginAdapter, AbstractUserClient
from api.client.http_client import HttpClient


class ClientAdapterTeamsOTP(HttpClient):
    __metaclass__ = AbstractLoginAdapter

    def __init__(self, base_url):
        super().__init__(base_url=base_url)

    def real_method(self):
        print("RealAdapter -> real_method")

    def login(self, parent_obj: "AbstractUserClient"):
        print(f"RealAdapter -> login -> parent_obj: {parent_obj}")
        self.real_method()
        parent_obj.real_method()
        parent_obj.aimsid = "TEST_!@#$%^&*()"

class ClientAdapterTeamsSWA(HttpClient):
    __metaclass__ = AbstractLoginAdapter

    def __init__(self, base_url: str):
        super().__init__(base_url=base_url)

    def real_method(self):
        print("RealAdapter -> real_method")

    def login(self, parent_obj: "AbstractUserClient"):
        print(f"RealAdapter -> login -> parent_obj: {parent_obj}")
        self.real_method()
        parent_obj.real_method()
        parent_obj.aimsid = "TEST_!@#$%^&*()"

class ClientAdapterTeamsSSO(HttpClient):
    __metaclass__ = AbstractLoginAdapter

    def __init__(self, base_url: str):
        super().__init__(base_url=base_url)

    def real_method(self):
        print("RealAdapter -> real_method")

    def login(self, parent_obj: "AbstractUserClient"):
        print(f"RealAdapter -> login -> parent_obj: {parent_obj}")
        self.real_method()
        parent_obj.real_method()
        parent_obj.aimsid = "TEST_!@#$%^&*()"


class ClientAdapterBiz(HttpClient):
    __metaclass__ = AbstractLoginAdapter

    def __init__(self, base_url):
        super().__init__(base_url=base_url)

    def auth_types(self, url: str):
        return self.get(url=f"{url}/api/domains/auth-types")

    def login(self, parent_obj: "AbstractUserClient"):
        print(f"RealAdapter -> login -> parent_obj: {parent_obj}")
        self.auth_types()
        parent_obj.real_method()

        parent_obj.aimsid = "TEST_!@#$%^&*()"


class ClientAdapterWs(HttpClient):
    __metaclass__ = AbstractLoginAdapter

    def __init__(self, base_url: str):
        super().__init__(base_url=base_url)
        self.base_url = base_url

    def auth_types(self, url: str):
        return self.get(url=f"{url}/api/domains/auth-types")

    def login(self, parent_obj: "AbstractUserClient"):
        print(f"RealAdapter -> login -> parent_obj: {parent_obj}")
        self.auth_types(url=self.base_url)
        parent_obj.aimsid = "TEST_!@#$%^&*()"

