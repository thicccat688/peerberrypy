from peerberry.exceptions import PeerberryException
import requests


class RequestHandler:
    def __init__(
            self,
            headers: dict,
    ):
        self.__session = requests.Session()
        self.__session.headers = headers

    def peerberry_request(
            self,
            url: str,
            params: str,
            data: dict,
            method: str = 'GET',
            **kwargs,
    ) -> dict:
        response = self.__session.request(
            method=method,
            url=url,
            params=params,
            data=data,
            **kwargs,
        )

        parsed_response = response.json()

        if response.status_code >= 400:
            raise PeerberryException(list(parsed_response['errors'].values())[0])

        return parsed_response
