import copy


class Utils:
    @staticmethod
    def parse_peerberry_items(__obj: dict) -> dict:
        parsed_obj = copy.deepcopy(__obj)

        for k, v in __obj.items():
            if isinstance(v, dict):
                nested_obj = {}

                for k1, v1 in v.items():
                    try:
                        nested_obj[k1] = float(v1)

                    except (ValueError, TypeError):
                        parsed_obj[k1] = v1

                parsed_obj[k] = nested_obj

                continue

            try:
                parsed_obj[k] = float(v)

            except (ValueError, TypeError):
                parsed_obj[k] = v

        return parsed_obj
