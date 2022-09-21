from peerberry.api import API
from datetime import date
import pandas as pd


email = str(input('Insert your email: '))
password = str(input('Insert your password: '))
tfa_secret = str(input('Insert your tfa token: '))


peerberry_client = API(
    email=email,
    password=password,
    tfa_secret=tfa_secret,
)


def test_profile():
    assert isinstance(peerberry_client.get_profile(), dict)


def test_loyalty():
    assert isinstance(peerberry_client.get_loyalty_tier(), dict)


def test_overview():
    assert isinstance(peerberry_client.get_overview(), dict)


def test_profit_overview():
    assert isinstance(
        peerberry_client.get_profit_overview(
            start_date=date(2022, 8, 21),
            finish_date=date(2022, 9, 21),
            periodicity='day',
            raw=False,
        ),
        pd.DataFrame,
    )


def test_investment_status():
    assert isinstance(peerberry_client.get_investment_status(), dict)


def test_loans():
    assert isinstance(
        peerberry_client.get_loans(
            quantity=10,
            sort='loan_amount',
            raw=False,
        ),
        pd.DataFrame,
    )
