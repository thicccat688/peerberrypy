from peerberry.exceptions import PeerberryException
from peerberry.constants import CONSTANTS
from typing import Type
import requests


class RequestHandler:
    def __init__(self):
        """ Request handler for internal use with Peerberry's specifications. """
        self.__session = requests.Session()

    def request(
            self,
            url: str,
            method: str = 'GET',
            exception_type: Type[Exception] = PeerberryException,
            output_type: str = 'json',
            **kwargs,
    ) -> any:
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
            error_response = response.json()

            raise exception_type(list(error_response['errors'].values())[0])

        return parsed_response

    def get_headers(self) -> object:
        return self.__session.headers

    def add_header(self, header: dict) -> object:
        self.__session.headers.update(header)

        return self.get_headers()

    def remove_header(self, key: str) -> object:
        self.__session.headers.pop(key, None)

        return self.get_headers()
