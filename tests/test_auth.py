from peerberry.auth import AuthHandler


def test_login():
    email = str(input('Insert your email:'))
    password = str(input('Insert your password:'))
    tfa_secret = str(input('Insert your tfa token:'))

    auth_client = AuthHandler(
        email=email,
        password=password,
        tfa_secret=tfa_secret,
    )

    assert isinstance(auth_client.get_access_token(), str)
