import re
from typing import Union, Literal, Optional


class BaseRequestException(Exception):
    def __init__(
        self,
        env: Literal["ICQ", "SAAS", "PRE_SAAS", "SANDBOX", "VKTI", "PRE_VKTI", "TARM", "PRE_TARM"],
        path_url: str,
        response_status_code: Union[str, int],
        response_status_text: str,
        http_request_plain_text: Optional[str],
    ):
        self.env = env
        self.path_url = path_url.split("?")[0]
        self.response_status_code = response_status_code
        self.response_status_text = response_status_text
        self.http_request_plain_text = http_request_plain_text
        super().__init__(self.get_error_message())

    def get_error_message(self) -> str:
        """
        Getting error message text
        """
        core_error_messge = ":".join(
            [
                self.env,
                self.path_url,
                str(self.response_status_code),
                self.response_status_text,
            ],
        )

        *_, real_path = re.split(r"/api/v[\d+]+", self.path_url)
        return """{core_error_messge}

Environment: {env}
URL: {path_url}
Response - Status code: {response_status_code}
Response - Status text: {response_status_text}

Failed request:
{http_request_plain_text}""".format(core_error_messge=core_error_messge, **self.__dict__)


class RequestException(BaseRequestException): ...


class RatelimitException(BaseRequestException): ...


class HttpNotFoundException(BaseRequestException): ...


class MissingParameterException(BaseRequestException): ...


class ServerException(BaseRequestException): ...


class BadGatewayException(BaseRequestException): ...


class AccessDeniedException(BaseRequestException): ...


class WAFRequestBlocked(BaseRequestException): ...


class BadRequestException(BaseRequestException): ...


class UserMustJoinByLinkException(BaseRequestException): ...


class OrgstructureException(BaseRequestException): ...


class SendImStateException(BaseRequestException): ...


class TooManyRedirectsException(BaseRequestException): ...


class ScheduledMessageAsRegularOne(BaseRequestException): ...


class GetHistoryException(BaseRequestException): ...


class ContactException(BaseRequestException): ...


class TaskCreationErrorException(BaseRequestException): ...


class PollCreationErrorException(BaseRequestException): ...


class MessageIsTooBigException(BaseRequestException): ...


class ScheduledTimeIsTooFarInFutureException(BaseRequestException): ...


class ScheduledMessagesLimitReachedException(BaseRequestException): ...


class MultipinLimitException(BaseRequestException): ...


class MultipinNotPaidException(BaseRequestException): ...


class BadTargetException(BaseRequestException): ...


class InvalidAimsidException(BaseRequestException): ...


class FederationReguestException(BaseRequestException): ...
