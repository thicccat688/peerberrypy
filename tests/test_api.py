from tests.constants import CONSTANTS
from peerberry.api import API

from datetime import date
import pandas as pd
import os


email = os.getenv(key='PEERBERRY_EMAIL')
password = os.getenv(key='PEERBERRY_PASSWORD')
tfa_secret = os.getenv(key='PEERBERRY_TFA_SECRET')


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
            end_date=date(2022, 9, 21),
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
            originators=['Aventus Group'],
            sort='loan_amount',
            raw=False,
        ),
        pd.DataFrame,
    )


def test_loan_details():
    assert isinstance(
        peerberry_client.get_loan_details(
            loan_id=1,
            raw=False,
        ),
        dict,
    )


def test_investments():
    assert isinstance(
        peerberry_client.get_investments(
            quantity=100,
            current=True,
            max_interest_rate=20,
            min_interest_rate=10,
            countries=['Kazakhstan', 'Lithuania'],
            raw=False,
        ),
        pd.DataFrame,
    )

    assert isinstance(
        peerberry_client.get_investments(
            quantity=100,
            current=False,
            max_interest_rate=20,
            min_interest_rate=10,
            countries=['Kazakhstan', 'Lithuania'],
            raw=False,
        ),
        pd.DataFrame,
    )

    assert isinstance(peerberry_client.get_mass_investments(raw=False), pd.DataFrame)


def test_summary():
    assert isinstance(
        peerberry_client.get_account_summary(
            start_date=CONSTANTS.START_DATE,
            end_date=CONSTANTS.END_DATE,
        ),
        dict,
    )


def test_transactions():
    assert isinstance(
        peerberry_client.get_transactions(
            quantity=1000,
            start_date=CONSTANTS.START_DATE,
            end_date=CONSTANTS.END_DATE,
            raw=False,
        ),
        pd.DataFrame,
    )

    assert isinstance(
        peerberry_client.get_mass_transactions(
            quantity=1000,
            start_date=CONSTANTS.START_DATE,
            end_date=CONSTANTS.END_DATE,
            raw=False,
        ),
        pd.DataFrame,
    )
