class BaseResponse:
    response: dict

    def __init__(self, response: dict):
        self.response = response

    @property
    def status(self) -> str | None:
        raise NotImplementedError

    @property
    def status_date(self) -> str | None:
        raise NotImplementedError

    @property
    def notification_id(self) -> str | None:
        raise NotImplementedError

    @property
    def notification_receiver_id(self) -> str | None:
        raise NotImplementedError


class BaseService:
    def __init__(self):
        pass

    def send(self, to: dict | list[dict], subject: str, body: str, notification_id: str = None, notification_receiver_id: str = None, webhook_url: str = None) -> BaseResponse:
        raise NotImplementedError

    def get_response(self, response: dict) -> BaseResponse:
        raise NotImplementedError
