from peerberry.exceptions import PeerberryException
from peerberry.constants import CONSTANTS
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
            output_type: str = 'json',
            **kwargs,
    ) -> Union[list, dict]:
        output_types = CONSTANTS.OUTPUT_TYPES
        output_type = output_type.lower()

        if output_type not in output_types:
            raise ValueError(f'Output type must be one of the following: {", ".join(output_types)}')

        response = self.__session.request(
            method=method,
            url=url,
            **kwargs,
        )

        if output_type == 'bytes':
            parsed_response = response.content

        else:
            parsed_response = response.json()

        if response.status_code >= 400:
            raise exception_type(response.json()['errors'][0]['message'])

        return parsed_response

    def get_headers(self) -> object:
        return self.__session.headers

    def add_header(self, header: dict) -> object:
        self.__session.headers.update(header)

        return self.get_headers()
