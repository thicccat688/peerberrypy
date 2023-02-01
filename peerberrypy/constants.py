from peerberrypy.exceptions import PeerberryException
from peerberrypy.endpoints import ENDPOINTS
import cloudscraper
import time


class CONSTANTS:
    GLOBALS, COUNTRIES_ISO, ORIGINATORS_ID = None, None, None

    PERIODICITIES = {'day', 'month', 'year'}

    TRANSACTION_PERIODICITIES = {'today', 'thisWeek', 'thisMonth'}

    OUTPUT_TYPES = {'json', 'bytes'}

    LOAN_TYPES_ID = {
        'short_term': 1,
        'long_term': 2,
        'real_estate': 3,
        'leasing': 4,
        'business': 5,
    }

    TRANSACTION_TYPES = {
        'deposit': 1,
        'withdrawal': 2,
        'principal_repayment': 3,
        'interest_payment': 4,
        'investment': 11,
        'fees_and_bonuses': 16,
    }

    TRANSACTION_SORT_TYPES = {
        'amount': 'Amount',
    }

    LOAN_SORT_TYPES = {
        'loan_id': 'loanId',
        'term': 'term',
        'issued_date': 'issuedDate',
        'interest_rate': 'interestRate',
        'loan_amount': 'availableToInvest',
    }

    CURRENT_INVESTMENT_SORT_TYPES = {
        'purchase_date': 'dateOfPurchcase',
        'interest_rate': 'interestRate',
        'loan_amount': 'amount',
        'estimated_final_payment_date': 'estimatedFinalPaymentDate',
    }

    FINISHED_INVESTMENT_SORT_TYPES = {
        'final_payment_date': 'finishedAt',
        'purchase_date': 'dateOfPurchcase',
        'interest_rate': 'interestRate',
        'loan_amount': 'amount',
        'estimated_final_payment_date': 'estimatedFinalPaymentDate',
    }

    LOAN_EXPORT_SORT_TYPES = {
        'date_of_purchase': 'Date of purchase',
        'interest_rate': 'Interest rate',
        'invested_amount': 'Invested amount',
        'estimated_final_payment_date': 'Estimated final payment date',
        'estimated_next_principal_payment': 'Estimated next payment (principal)',
        'estimated_next_interest_payment': 'Estimated next payment (interest)',
        'term_until_estimated_payment_date': 'Left term till estimated payment date',
        'received_payments': 'Received payments',
        'last_received_payment_date': 'Last received payment date',
        'remaining_principal': 'Remaining principal',
        'status': 'Status',
    }
    
    _session = cloudscraper.create_scraper(
        browser={
            'browser': 'chrome',
            'platform': 'windows',
            'desktop': True,
        }
    )

    @classmethod
    def get_globals(cls) -> dict:
        if cls.GLOBALS is None:
            response = cls._session.get(ENDPOINTS.GLOBALS_URI, params={'t': int(time.time())})

            if response.status_code != 200:
                raise PeerberryException('Failed to fetch globals.')

            cls.GLOBALS = response.json()

        return cls.GLOBALS

    @classmethod
    def get_countries(cls) -> dict:
        if cls.COUNTRIES_ISO is None:
            cls.COUNTRIES_ISO = dict(
                map(
                    lambda cnt: (cnt['title'].strip(), {k: v for k, v in cnt.items() if k != 'title'}),
                    cls.get_globals()['countries'],
                )
            )

        return cls.COUNTRIES_ISO

    @classmethod
    def get_originators(cls) -> dict:
        if cls.ORIGINATORS_ID is None:
            cls.ORIGINATORS_ID = dict(
                map(
                    lambda org: (
                        org['title'].strip(),
                        {k: v for k, v in org.items() if k != 'title'},
                    ),
                    cls.get_globals()['originators']
                )
            )

        return cls.ORIGINATORS_ID

    @classmethod
    def get_country_iso(cls, country: str) -> int:
        if cls.COUNTRIES_ISO is None:
            cls.get_countries()

        if country not in cls.COUNTRIES_ISO:
            raise ValueError(
                f'{country} must be one of the following countries: {", ".join(cls.COUNTRIES_ISO)}.',
            )

        return cls.COUNTRIES_ISO[country].get('id')

    @classmethod
    def get_originator(cls, originator: str) -> int:
        if cls.ORIGINATORS_ID is None:
            cls.get_originators()

        if originator not in cls.ORIGINATORS_ID:
            raise ValueError(
                f'{originator} must be one of the following originators: {", ".join(cls.ORIGINATORS_ID)}.',
            )

        return cls.ORIGINATORS_ID[originator].get('id')
