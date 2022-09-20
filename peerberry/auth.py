from peerberry.endpoints import ENDPOINTS
from peerberry.exceptions import InvalidCredentials
import requests
import pyotp


class AuthHandler:
    def __init__(
            self,
            email: str,
            password: str,
            tfa_secret: str = None,
    ):
        self.email = email
        self.__password = password
        self.__tfa_secret = tfa_secret

    def get_access_token(self) -> str:
        login_data = {
            'email': self.email,
            'password': self.__password,
        }

        login_response = requests.post(
            url=ENDPOINTS.LOGIN_URI,
            data=login_data,
        )

        parsed_login_response = login_response.json()

        if login_response.status_code != 200:
            raise InvalidCredentials(parsed_login_response['message'])

        tfa_response_token = parsed_login_response.get('tfa_token')

        if self.__tfa_secret is None:
            return f'Bearer {tfa_response_token}'

        totp_data = {
            'code': pyotp.TOTP(self.__tfa_secret).now(),
            'tfa_token': tfa_response_token,
        }

        totp_response = requests.post(
            url=ENDPOINTS.TFA_URI,
            data=totp_data,
        )

        parsed_totp_response = totp_response.json()

        if totp_response.status_code != 200:
            raise InvalidCredentials(parsed_totp_response['message'])

        access_token = parsed_totp_response.get('access_token')

        # Set authorization header with JWT bearer token
        return f'Bearer {access_token}'
