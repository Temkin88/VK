from __future__ import annotations

from datetime import datetime
from typing import Optional, List, Union, TypedDict, Unpack, Any
from uuid import uuid1

from api.client.http_client import HttpClient


class ScheduleArg(TypedDict):
    scheduledTime: int
    updateScheduledMsgId: Optional[int | str]


class RapiMsgSendBaseKwargs(TypedDict, total=True):
    updateMsgId: Optional[int | str]
    draftDeleteTime: Optional[int]
    localMsgId: Optional[str]
    schedule: ScheduleArg


class RapiMsgSendNoPartsKwargs(RapiMsgSendBaseKwargs, total=False):
    mainPart: Optional[dict[str, Any]]
    quoteParts: Optional[list[dict[str, Any]]]
    forwardParts: Optional[list[dict[str, Any]]]


class RapiMsgSendPartsKwargs(RapiMsgSendBaseKwargs):
    parts: RapiMsgSendNoPartsKwargs


class MessagesMethods(HttpClient):
    """
    Методы группы 'Сообщения' из https://im-docs.corp.mail.ru/
    """
    def getReqId(self) -> str:
        """
        Генерация уникального ID запроса
        :return: str
        """
        return str(uuid1())
    
    def rapi_getHistory(
        self,
        sn: str,
        url: str,
        api_version: int,
        aimsid: str,
        fromMsgId: Union[str, int] = "-1",
        count: int = -20,
        patchVersion: str = "init",
        tillMsgId: Optional[int] = None,
        onlyDelMsgs: Optional[bool] = False,
        lang: str = "ru-ru",
        mentions_resolve: bool = True,
    ) -> dict:
        """
        Получить историю сообщений
        :param sn: Sn собеседника
        :param fromMsgId: Id сообщения,
        начиная с которого будет запрашиваться история
        (НЕ будет включено в итогувую выборку сообщений)
        :param count: Максимальное число сообщений в истории.
        Если положительное, то выбираются сообщения,
        новее чем fromMsgId, если отрицательное - старее.
        :param patchVersion: Последний полученный patchVersion.
        Если не был получен, следует выставить значение "none"
        :param tillMsgId: Id сообщения,
        до которого будет запрашиваться история
        (НЕ будет включено в итогувую выборку сообщений)
        :param onlyDelMsgs: Получить только удаленные сообщения
        (только для админов и prismtoken)
        :param lang: Локаль клиента, формат 'язык-страна',
        для перевода системных сообщений.
        :param mentions_resolve: Отображать
        friendly name вместо sn при упоминаниях
        :return: тело ответа сервера
        """
        return self.post(
            url=url + f"/api/v{api_version}/rapi/getHistory",
            headers={"Content-Type": "application/json"},
            json={
                "aimsid": aimsid,
                "reqId": self.getReqId(),
                "params": {
                    "sn": sn,
                    "fromMsgId": fromMsgId,
                    "count": count,
                    "tillMsgId": tillMsgId,
                    "patchVersion": patchVersion,
                    "onlyDelMsgs": onlyDelMsgs,
                    "lang": lang,
                    "mentions": {"resolve": mentions_resolve},
                },
            },
        )

    def rapi_delMsgBatch(
        self,
        sn: str,
        url: str,
        api_version: int,
        aimsid: str,
        msgIds: List[int],
        shared: bool = True,
        silent: bool = True,
    ) -> dict:
        """
        Удалить набор сообщений
        :param sn: Sn собеседника/чата
        :param msgIds: Массив msgId сообщений, которые необходимо удалить
        :param shared: Удалить для всех
        :param silent: Просьба удаления без нотификации и системной заглушки
        (для тихого удаления shared флаг так же должен быть выставлен в true)
        :return: тело ответа сервера
        """
        return self.post(
            url=url + f"/api/v{api_version}/rapi/delMsgBatch",
            headers={"Content-Type": "application/json"},
            json={
                "aimsid": aimsid,
                "reqId": self.getReqId(),
                "params": {
                    "sn": sn,
                    "msgIds": msgIds,
                    "shared": shared,
                    "silent": silent,
                },
            },
        )

    def rapi_setDlgState(
        self,
        sn: str,
        url: str,
        api_version: int,
        aimsid: str,
        stranger: bool = False,
        exclude: List[str] = (),
        lastRead: int = -1,
    ) -> dict:
        """
        Изменить состояние диалога
        :param sn: Sn собеседника
        :param stranger: Неизвестный диалог
        :param exclude: call | text | mention | pttListen
        :param lastRead: msgId последнего прочитанного сообщения
        :return: тело ответа сервера
        """
        return self.post(
            url=url + f"/api/v{api_version}/rapi/setDlgState",
            headers={"Content-Type": "application/json"},
            json={
                "aimsid": aimsid,
                "reqId": self.getReqId(),
                "params": {
                    "sn": sn,
                    "stranger": stranger,
                    "exclude": exclude,
                    "lastRead": lastRead,
                },
            },
        )

    def rapi_draft_set(
        self,
        sn: str,
        parts: list[dict],
        url: str,
        api_version: int,
        aimsid: str,
        mentions: Optional[list[str]] = None
    ) -> dict:
        """
        Черновик может содержать только текст
        (part с mediaType=text, поле text)
        или ответ на сообщение (part с mediaType=quote)

        Чтобы удалить черновик, нужно отправить запрос с пустым массивом parts
        :param sn: Уникальный идентификатор пользователя или группы/канала
        :param parts: Массив parts — это составные части,
        из которых состоит отправляемое сообщение.
        Может содержать текст или ответ на другие сообщения.
        :param mentions: Список пользователей,
        которые были упомянуты в черновике
        :return: тело ответа сервера
        """
        return self.post(
            url=url + f"/api/v{api_version}/rapi/draft/set",
            headers={"Content-Type": "application/json"},
            json={
                "aimsid": aimsid,
                "reqId": self.getReqId(),
                "params": {
                    "sn": sn,
                    "time": int(datetime.now().timestamp()),
                    "parts": parts,
                    "mentions": mentions if mentions is not None else [],
                },
            },
        )

    def rapi_pinMessage(
        self,
        sn: str,
        msgId: Union[str, int],
        url: str,
        api_version: int,
        aimsid: str,
        unpin: bool = False
    ) -> dict:
        """
        Закрепить/открепить сообщение в чате
        """
        return self.post(
            url=url + f"/api/v{api_version}/rapi/pinMessage",
            headers={"Content-Type": "application/json"},
            json={
                "aimsid": aimsid,
                "reqId": self.getReqId(),
                "params": {"sn": sn, "msgId": msgId, "unpin": unpin},
            },
        )

    def rapi_message_send(
        self,
        target: str,
        url: str,
        api_version: int,
        aimsid: str,
        **kwargs: Unpack[RapiMsgSendPartsKwargs],
    ) -> dict:
        """
        :param target:Уникальный идентификатор пользователя или чата внутри сервиса,
         которому отправляем сообщение.
        :param parts: объект с main_part и массивами quote_parts и forward_parts внутри
        :param main_part: Парт для основной части сообщения (не пересланное и не ответ)
        Параметр используется для отправки текста, медиа-объектов,
        опросов, контактов, местоположения и т. д.
        :param quote_parts: Массив, состоящий из элементов quotePart для пересланных сообщений.
        Каждый из элементов quotePart состоит из партов оригинального сообщения,
        id существующего сообщения, id существующего опроса и тд
        :param forward_parts: Массив, состоящий из элементов forwardPart для пересланных сообщений.
        ForwardPart отличается от QuotePart возможным наличием объекта chat, если пересылаем из чата
        :param aimsid: Идентификатор пользовательской сессии, полученный в результате выполнения
        запроса /wim/aim/startSession
        :param update_msg_id: Id редактируемого сообщения
        :param draft_delete_time: Время отправки сообщения, если оно было черновиком
        :param schedule: объект для запланированных - состоит из 2 полей
            scheduledTime - обязательное поле, timestamp запланированного времени отправки
            updateScheduledMsgId - используется для редактирования запланированного в очереди
        :param localMsgId: при получении этого поля оно будет использовано вместо reqId для текущего запроса.
            Необходимо для предотвращения дублирования сообщений на некоторых клиентах.
            LocalMsgId- это сгенерированный на клиенте временный идентификатор сообщения,
                используемый локально на клиенте до момента получения msgId от сервера.
            Серверный msgId может быть получен из тела ответа message/send, а также из некоторых ивентов,
                приходящих в теле ответа fetchEvents.
            При получении ивентов histDlgState/imState поле reqId/sendReqId соответственно будет совпадать с localMsgId,
             что позволит избежать дублирования сообщений.
        :return: тело ответа сервера
        """
        sub_chats = set()
        sub_chats.add(target)

        def delete_nulls(item):
            if not isinstance(item, dict):
                return item

            for key, value in item.copy().items():
                if value is None:
                    del item[key]
                elif isinstance(value, dict):
                    if value := delete_nulls(value):
                        item[key] = value
                elif isinstance(value, list):
                    item[key] = [delete_nulls(i) for i in value]
                else:
                    continue
            return item

        kwargs = delete_nulls(kwargs)

        return self.post(
            url=url + f"/api/v{api_version}/rapi/message/send",
            json={
                "aimsid": aimsid,
                "reqId": self.getReqId(),
                "params": {"target": target, **kwargs},
            },
        )

    def rapi_message_scheduled_cancel(
        self,
        sn: str,
        url: str,
        api_version: int,
        aimsid: str,
        scheduled_msg_ids: Optional[list[str | int]] = None
    ):
        """
        Отменить отправку запланированных (удалить).
        :param sn: ID чата
        :param scheduled_msg_ids: ID запланированных сообщений
        """
        params = {"sn": sn}

        if not scheduled_msg_ids:
            params["cancelAll"] = True
        else:
            params["scheduledMsgIds"] = scheduled_msg_ids

        return self.post(
            url=url + f"/api/v{api_version}/rapi/message/scheduled/cancel",
            headers={"Content-Type": "application/json"},
            json={
                "aimsid": aimsid,
                "reqId": self.getReqId(),
                "params": params,
            },
        )

    def rapi_message_scheduled_flush(
        self,
        sn: str,
        scheduled_msg_ids: list[str | int],
        url: str,
        api_version: int,
        aimsid: str,
    ):
        """
        Отправить запланированные,
        которые в текущий момент находятся
        в очереди запланированных мгновенно сейчас.
        :param sn: ID чата
        :param scheduled_msg_ids: ID запланированных сообщений
        """
        return self.post(
            url=url + f"/api/v{api_version}/rapi/message/scheduled/flush",
            headers={"Content-Type": "application/json"},
            json={
                "aimsid": aimsid,
                "reqId": self.getReqId(),
                "params": {"sn": sn, "scheduledMsgIds": scheduled_msg_ids},
            },
        )

    def rapi_message_scheduled_history_get(
        self,
        sn: str,
        url: str,
        api_version: int,
        aimsid: str,
        history_version: str = "0"
    ):
        """
        Отправить запланированные,
        которые в текущий момент находятся
        в очереди запланированных мгновенно сейчас.
        :param sn: ID чата
        :param history_version: Версия истории (очереди) запланированных.
        Строка в запросах, но по факту число.
        """
        return self.post(
            url=url + f"/api/v{api_version}/rapi/message/scheduled/history/get",
            headers={"Content-Type": "application/json"},
            json={
                "aimsid": aimsid,
                "reqId": self.getReqId(),
                "params": {"sn": sn, "historyVersion": history_version},
            },
        )

    def rapi_receivedMessages(
        self,
        sn: str,
        msg_ids: list[int | str],
        url: str,
        api_version: int,
        aimsid: str,
    ):
        return self.post(
            url=url + f"/api/v{api_version}/rapi/receivedMessages",
            headers={"Content-Type": "application/json"},
            json={
                "aimsid": aimsid,
                "reqId": self.getReqId(),
                "params": {"dialogs": [{"sn": sn, "msgIds": msg_ids}]},
            },
        )
