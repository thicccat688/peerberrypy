import copy
from decimal import Decimal, DecimalException


class Utils:
    @staticmethod
    def parse_peerberry_items(__obj: dict) -> dict:
        parsed_obj = copy.deepcopy(__obj)

        for k, v in __obj.items():
            if isinstance(v, dict):
                nested_obj = {}

                for k1, v1 in v.items():
                    try:
                        nested_obj[k1] = Decimal.from_float(v1) if isinstance(v1, float) else Decimal(v1)

                    except (ValueError, TypeError, DecimalException):
                        parsed_obj[k1] = v1

                parsed_obj[k] = nested_obj

                continue

            try:
                parsed_obj[k] = Decimal.from_float(v) if isinstance(v, float) else Decimal(v)

            except (ValueError, TypeError, DecimalException):
                parsed_obj[k] = v

        return parsed_obj

    @staticmethod
    def parse_peerberry_originators(__obj: list) -> dict:
        parsed_obj = {}

        for i in __obj:
            parsed_obj[i['originator']] = i

        return parsed_obj