from peerberry.endpoints import ENDPOINTS
from peerberry.auth import AuthHandler
import pandas as pd
import requests


class API:
    def __init__(
            self,
            email: str,
            password: str,
            tfa_secret: str = None,
    ):
        # Initialize authentication client
        self.__auth_client = AuthHandler(
            email=email,
            password=password,
            tfa_secret=tfa_secret,
        )

        # Initialize API session, authenticate & get access token
        self.__session = requests.Session()
        self.__session.headers['Authorization'] = self.__auth_client.get_access_token()

    def get_overview(self) -> dict:
        return {}
