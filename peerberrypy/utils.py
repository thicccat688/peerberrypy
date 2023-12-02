import copy
from decimal import Decimal, DecimalException


class Utils:
    @staticmethod
    def parse_peerberry_items(obj: dict) -> dict:
        """Parse string represenations of decimals and floats into Decimal"""
        if isinstance(obj, list):
            return [Utils.parse_peerberry_items(item) for item in obj]
        elif isinstance(obj, dict):
            return {k: Utils.parse_peerberry_items(v) for k, v in obj.items()}
        elif isinstance(obj, (Decimal, int)):
            return obj
        elif isinstance(obj, float):
            return Decimal.from_float(obj)
        elif isinstance(obj, str) and obj.startswith('+'):
            # preserve phone numbers
            return obj
        else:
            try:
                return Decimal(obj)
            except (ValueError, TypeError, DecimalException):
                pass

        return obj
