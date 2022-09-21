from typing import Generator


class CONSTANTS:
    PERIODICITIES = {'day', 'month', 'year'}

    COUNTRIES_ISO = {
        'Lithuania': 1,
        'Poland': 2,
        'Czech Republic': 63,
        'Kazakhstan': 118,
        'Moldova': 149,
        'Philippines': 178,
        'Romania': 185,
        'Russian Federation': 186,
        'Sri Lanka': 213,
        'Ukraine': 236,
        'Vietnam': 245,
    }

    ORIGINATORS_BRANDS = {
        'Aventus Group',
        'Gofingo Group',
        'Lithome',
        'SIB Group',
        'Aventus Development',
        'Litelektra',
    }

    ORIGINATORS_ID = {
        'Aventus Group': {
            'Smart Pozczka PL': 2,
            'Pozyczka Plus PL': 3,
            'Pozyczka Plus PL - personal loans': 8,
            'Smart Pozczka PL - personal loans': 9,
            'Auto-Money KZ': 12,
            'Auto Money UA': 13,
            'Slon Credit UA': 14,
            'Credit plus UA': 15,
            'Credit7 MD': 18,
            'Belka Credit RU': 20,
            'Credit7 UA': 21,
            'Credit365 MD': 23,
            'Senmo VN': 28,
            'Credit Plus KZ': 30,
            'Nano deneg RU': 31,
            'Credit7 RU': 32,
            'Cash X LK': 33,
            'Credit365 KZ': 36,
            'LLC Selfie credit': 37,
            'Selfie credit LLC': 38,
            'CashXpress PH': 39,
            'Credit7 RO': 42,
            'LendPlus': 43,
            'Dong Plus VN': 44,
        },
        'Gofingo Group': {
            'Sos Credit CZ': 4,
            'Euro Groshi LLC': 6,
            'Gofingo UA': 19,
            'Euro Groshi UA': 22,
            'Zecredit UA': 27,
        },
        'Lithome': {
            'Lithome LT': 7,
        },
        'SIB Group': {
            'Si Baltic LLC': 29,
            'LLC Teratus': 34,
            'LLC Pakrantės būstas': 35,
        },
        'Aventus Development': {
            'Aldega LLC': 40,
        },
        'Litelektra': {
            'Litelektra': 41,
        }
    }

    LOAN_SORT_TYPES = {
        'loan_id': 'loanId',
        'term': 'term',
        'issued_date': 'issuedDate',
        'interest_rate': 'interestRate',
        'loan_amount': 'availableToInvest',
    }

    @classmethod
    def get_originators(cls) -> dict:
        return {k: v for (k, v) in cls.get_values(cls.ORIGINATORS_ID)}

    @classmethod
    def get_values(cls, __obj: dict) -> Generator:
        for (k, v) in __obj.items():
            if isinstance(v, dict):
                yield k, list(__obj[k].values())

                yield from cls.get_values(v)

            else:
                yield k, v
