from peerberry.exceptions import PeerberryException
from typing import Union, Type
import requests


class RequestHandler:
    def __init__(self):
        self.__session = requests.Session()

    def request(
            self,
            url: str,
            method: str = 'GET',
            exception_type: Type[Exception] = PeerberryException,
            **kwargs,
    ) -> Union[list, dict]:
        response = self.__session.request(
            method=method,
            url=url,
            **kwargs,
        )

        parsed_response = response.json()

        if response.status_code >= 400:
            raise exception_type(parsed_response['errors'][0]['message'])

        return parsed_response

    def get_headers(self) -> object:
        return self.__session.headers

    def add_header(self, header: dict) -> object:
        self.__session.headers.update(header)

        return self.get_headers()
