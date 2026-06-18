from typing import TypedDict, Unpack
from uuid import uuid1

from api.client.http_client import HttpClient


class SearchChatThreadsKwargs(TypedDict):
    after: str
    before: str


class SearchMethods(HttpClient):
    """
    Методы группы 'Поиск' из https://im-docs.corp.mail.ru/
    """
    def getReqId(self) -> str:
        """
        Генерация уникального ID запроса
        :return: str
        """
        return str(uuid1())
    
    def rapi_search(
        self,
        url: str,
        api_version: int,
        keyword: str,
        aimsid: str,
        withoutBlocked: bool = False,
        withoutBots: bool = False,
    ) -> dict:
        """
        Поиск
        :return: тело ответа сервера
        """
        return self.post(
            url=url + f"/api/v{api_version}/rapi/search",
            headers={"Content-Type": "application/json"},
            json={
                "reqId": self.getReqId(),
                "aimsid": aimsid,
                "params": {
                    "keyword": keyword,
                    "withoutBlocked": withoutBlocked,
                    "withoutBots": withoutBots,
                },
            },
        )

    def rapi_searchThreadsFeed(
        self,
        keyword: str,
        url: str,
        api_version: int,
        aimsid: str,
        pagesize: int = 50,
    ):
        """
        Поиск по потоку тредов
        """
        return self.post(
            url=url + f"/api/v{api_version}/rapi/searchThreadsFeed",
            headers={"Content-Type": "application/json"},
            json={
                "reqId": self.getReqId(),
                "aimsid": aimsid,
                "params": {
                    "pagesize": pagesize,
                    "filter": {"keyword": keyword},
                },
            },
        )

    def rapi_searchChatThreads(
        self,
        sn: str,
        url: str,
        api_version: int,
        aimsid: str,
        keyword: str,
        author: str,
        pagesize: int = 50,
        **kwargs: Unpack[SearchChatThreadsKwargs]
    ):
        r"""
        Ппоиск по сообщениям среди тредов указанного чата
        По самому чату поиск не осуществляется.
        :param sn: id чата для поиска
        :param pagesize: количество совпадений в выдаче
        :param keyword: текст для поиска
        :param author: screenname автора искомого сообщения (experimental)
        param after: дата в формате dd.mm.yyyy \n
        param before: дата в формате dd.mm.yyyy \n
        :return: тело ответа сервера
        """
        return self.post(
            url=url + f"/api/v{api_version}/rapi/searchChatThreads",
            headers={"Content-Type": "application/json"},
            json={
                "reqId": self.getReqId(),
                "aimsid": aimsid,
                "params": {
                    "pagesize": pagesize,
                    "filter": {
                        "keyword": keyword,
                        "author": author,
                        "data": {**kwargs},
                    },
                    "sn": sn,
                },
            },
        )

    def rapi_searchAllDialogs(
            self,
            filter_keyword: str,
            url: str,
            api_version: int,
            aimsid: str,
            mentions_resolve: bool = True
    ) -> dict:
        """
        Поиск по всем диалогам
        """
        return self.post(
            url=url + f"/api/v{api_version}/rapi/searchAllDialogs",
            headers={"Content-Type": "application/json"},
            json={
                "reqId": self.getReqId(),
                "aimsid": aimsid,
                "params": {
                    "filter": {"keyword": filter_keyword},
                    "mentions": {"resolve": mentions_resolve},
                },
            },
        )

    def rapi_searchOneDialog(
        self,
        chatId: str,
        filter_keyword: str,
        url: str,
        api_version: int,
        aimsid: str,
        mentions_resolve: bool = True
    ) -> dict:
        """
        Поиск по определенному чату/треду
        """
        return self.post(
            url=url + f"/api/v{api_version}/rapi/searchOneDialog",
            headers={"Content-Type": "application/json"},
            json={
                "reqId": self.getReqId(),
                "aimsid": aimsid,
                "params": {
                    "filter": {"keyword": filter_keyword},
                    "mentions": {"resolve": mentions_resolve},
                    "pagesize": 50,
                    "sn": chatId,
                },
            },
        )
