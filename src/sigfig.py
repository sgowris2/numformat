from decimal import Decimal


class SigFig:

    def to_precision(self, value, precision=None):
        if value == 0:
            return 0
        n = self._SigFig__get_sigfigs(value)

    # Private Methods

    @staticmethod
    def __convert_to_float(value):
        if type(value) in (int, float):
            return float(value)
        raise ValueError('Could not load input - {}'.format(value))

    @staticmethod
    def __get_sigfigs(value, strict=False):

        if isinstance(value, int):
            return SigFig.__get_sigfigs_for_integer_string(value)
        if isinstance(value, float):
            return SigFig.__get_sigfigs_for_decimal_string(value)
        if isinstance(value, str):
            value = value.strip().strip('-')
            if value.isdigit():
                value = int(value)
                return SigFig.__get_sigfigs_for_integer_string(value)
            else:
                value = SigFig.__to_decimal(value)
            return SigFig.__get_sigfigs_for_decimal_string(value)

        raise ValueError('Could not find sigfigs for input - {}'.format(value))

    @staticmethod
    def __to_decimal(value):
        try:
            value = Decimal(value)
        except:
            raise ValueError('Input is not a valid number - {}'.format(value))
        return value

    @staticmethod
    def __get_sigfigs_for_integer_string(value):
        return len(str(abs(value)).strip('0'))

    @staticmethod
    def __get_sigfigs_for_decimal_string(value):
        value_str = str(abs(value))
        decimal_point_index = len(value_str.split('.')[0])
        for i in range(len(value_str)):
            if value_str[i].isdigit():
                if value_str[i] != '0':
                    return len(value_str) - i - (1 if i < decimal_point_index else 0)
        return 0
