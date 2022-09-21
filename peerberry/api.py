from peerberry.endpoints import ENDPOINTS
from peerberry.request_handler import RequestHandler
from peerberry.exceptions import InvalidCredentials, InvalidPeriodicity
from peerberry.constants import CONSTANTS
from datetime import date
from typing import Union
import pandas as pd
import pyotp
import math


class API:
    def __init__(
            self,
            email: str,
            password: str,
            tfa_secret: str = None,
    ):
        self.email = email
        self.__password = password
        self.__tfa_secret = tfa_secret

        # Initialize API session, authenticate & get access token
        self.__session = RequestHandler()
        self.__session.add_header({'Authorization': self.__get_access_token()})

    def get_profile(self) -> dict:
        return self.__session.request(
            url=ENDPOINTS.PROFILE_URI,
        )

    def get_loyalty_tier(self) -> dict:
        response = self.__session.request(
            url=ENDPOINTS.LOYALTY_URI,
        )

        # Remove all tiers with locked set to true
        unlocked_tiers = list(filter(lambda obj: obj['locked'] is False, response['items']))

        # Get the highest unlocked tier
        top_available_tier = unlocked_tiers[-1]

        return {
            'tier': top_available_tier['title'].rstrip(),
            'extra_return': top_available_tier['percent'],
            'max_amount': top_available_tier['maxAmount'],
            'min_amount': top_available_tier['minAmount'],
        }

    def get_overview(self) -> dict:
        return self.__session.request(
            url=ENDPOINTS.OVERVIEW_URI,
        )

    def get_profit_overview(
            self,
            start_date: date,
            finish_date: date,
            periodicity: str = 'day',
            raw: bool = False,
    ) -> Union[pd.DataFrame, list]:
        """
        :param start_date: First date of profit data
        :param finish_date: Final date of profit data
        :param periodicity: Intervals to get profit data from (Daily, monthly or on a yearly basis)
        :param raw: Option to return raw python list or pandas DataFrame (False by default, so it returns a DataFrame)
        :return: Returns profit overview for portfolio on a daily, monthly or yearly basis
        """

        periodicites = CONSTANTS.PERIODICITIES

        if periodicity not in periodicites:
            raise InvalidPeriodicity(f'Periodicity must be one of the following: {", ".join(periodicites)}')

        profit_overview = self.__session.request(
            url=f'{ENDPOINTS.PROFIT_OVERVIEW_URI}/{start_date}/{finish_date}/{periodicity}',
        )

        return profit_overview if raw else pd.DataFrame(data=profit_overview)

    def get_investment_status(self) -> dict:
        return self.__session.request(
            url=ENDPOINTS.INVESTMENTS_STATUS_URI,
        )

    def get_loans(
            self,
            quantity: int,
            countries: list = None,
            loan_types: list = None,
            sort: str = 'loan_amount',
            ascending_sort: bool = False,
            raw: bool = False,
    ) -> Union[pd.DataFrame, list]:
        """
        :param quantity: Amount of loans to fetch
        :param countries: Filter loans by country of origin (Gets loans from all countries by default)
        :param loan_types: Filter loans by type (Short-term, long-term, real estate, leasing, and business)
        :param sort: Sort by loan attributes (By amount available for investment, interest rate, term, etc.)
        :param ascending_sort: Sort by ascending order (By default sorts in descending order)
        :param raw: Option to return raw python list or pandas DataFrame (False by default, so it returns a DataFrame)
        :return: Returns all available loans for investment according to specified parameters
        """

        loan_params = {
            'sort': sort if ascending_sort else f'-{sort}',
            'pageSize': 40 if quantity > 40 else quantity,
            'offset': 0,
        }

        # Add country filters to query parameters
        if countries:
            for idx, country in enumerate(countries):
                loan_params[f'countryIds[{idx}]'] = CONSTANTS.COUNTRIES_ISO[country]

        # Add loan type filters to query parameters
        if loan_types:
            for idx, type_ in enumerate(loan_types):
                loan_params[f'loanTermId[{idx}]'] = CONSTANTS.LOAN_SORT_TYPES[type_]

        loans = []

        for _ in range(math.ceil(quantity / 40)):
            loans_data = self.__session.request(
                url=ENDPOINTS.LOANS_URI,
                params=loan_params,
            )['data']

            # Extend current loan list with new loans
            loans.extend(loans_data)

            loan_params['offset'] += 40

        return loans if raw else pd.DataFrame(loans)

    def purchase_loan(
            self,
            loan_id: int,
            amount: int,
    ) -> str:
        """
        :param loan_id: ID of loan to purchase
        :param amount: Amount to invest in loan (Amount denominated in €)
        :return: Returns success message upon purchasing loan
        """

        self.__session.request(
            url=f'{ENDPOINTS.LOANS_URI}/{loan_id}',
            method='POST',
            data={'amount': str(amount)},
        )

        return f'Successfully invested €{amount} in loan {loan_id}.'

    def __get_access_token(self) -> str:
        login_data = {
            'email': self.email,
            'password': self.__password,
        }

        login_response = self.__session.request(
            url=ENDPOINTS.LOGIN_URI,
            method='POST',
            data=login_data,
            exception_type=InvalidCredentials,
        )

        tfa_response_token = login_response.get('tfa_token')

        if self.__tfa_secret is None:
            return f'Bearer {tfa_response_token}'

        totp_data = {
            'code': pyotp.TOTP(self.__tfa_secret).now(),
            'tfa_token': tfa_response_token,
        }

        totp_response = self.__session.request(
            url=ENDPOINTS.TFA_URI,
            method='POST',
            data=totp_data,
        )

        access_token = totp_response.get('access_token')

        # Set authorization header with JWT bearer token
        return f'Bearer {access_token}'


client = API(
    email='marcoperestrello@gmail.com',
    password='%kPevYbI6faQ0165pc24',
    tfa_secret='34KHNWOD326XBCEQIKRZ7HMDOY6WUY5A',
)

print(client.get_profile())
print(client.get_overview())
print(client.get_profit_overview(start_date=date(2022, 8, 21), finish_date=date(2022, 9, 21)))
print(client.get_loyalty_tier())
print(client.get_investment_status())
print(client.get_loans(quantity=100))
