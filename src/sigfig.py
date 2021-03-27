from decimal import Decimal
from math import floor, log10


class SigFig:

    @staticmethod
    def sfformat(value, max_sig_figs: int = None,
                 max_str_length: int = None,
                 allow_scientific_notation: bool = True):
        SigFig.__check_sfformat_args(max_sig_figs=max_sig_figs,
                                     max_str_length=max_str_length,
                                     allow_scientific_notation=allow_scientific_notation)

        value = SigFig._SigFig__convert_to_numeric(value)

        sig_figs = SigFig._SigFig__get_sigfigs(value)

        value_str = SigFig.__convert_to_desired_sigfigs_str(max_sig_figs, sig_figs, value)

        if max_str_length is not None:
            if len(value_str) <= max_str_length:
                return value_str

        return value_str

    # Private Methods

    @staticmethod
    def __convert_to_desired_sigfigs_str(max_sig_figs, sig_figs, value):
        if max_sig_figs is not None:
            if max_sig_figs >= sig_figs:
                return str(value)
            else:
                order = SigFig.__get_order(value)
                value = round(value, max_sig_figs - order)
                if (value % 1) == 0:
                    value = int(value)
                return str(value)
        return str(value)

    @staticmethod
    def __get_sigfigs(value):

        if isinstance(value, int):
            return SigFig.__get_sigfigs_for_integer(value)
        if isinstance(value, Decimal):
            return SigFig.__get_sigfigs_for_decimal(value)

        raise ValueError('Could not find sigfigs for input - {}'.format(value))

    @staticmethod
    def __get_order(value):
        if abs(float(value) - 0.0) < 0.000000001:
            return 0
        order = floor(log10(abs(value))) + 1
        return order

    @staticmethod
    def __convert_to_numeric(value):
        if isinstance(value, int):
            return value
        elif isinstance(value, float):
            value = SigFig.__to_decimal(repr(value))
            return value
        elif isinstance(value, str):
            digits_only_value = value.strip().strip('-')
            if digits_only_value.isdigit():
                value = int(value)
            else:
                value = SigFig.__to_decimal(value)
            return value
        else:
            raise ValueError('Input was not in any of the supported formats '
                             'int, float, decimal.Decimal. Received object of type {}'.format(type(value)))

    @staticmethod
    def __check_sfformat_args(max_sig_figs: int = None,
                              max_str_length: int = None,
                              allow_scientific_notation: bool = True):
        if max_sig_figs is not None and max_sig_figs < 1:
            raise ValueError('\'max_sig_figs\' must be >= 1. Received {}'.format(max_sig_figs))
        if max_str_length is not None and max_str_length < 3:
            raise ValueError('\'max_str_length\' must be >= 3. Received {}'.format(max_sig_figs))
        if not isinstance(allow_scientific_notation, bool):
            raise ValueError(
                '\'allow_scientific_notation\' must be a boolean. Received {}'.format(allow_scientific_notation))

    @staticmethod
    def __to_decimal(value):
        try:
            value = Decimal(value)
        except:
            raise ValueError('Input is not a valid number - {}'.format(value))
        return value

    @staticmethod
    def __get_sigfigs_for_integer(value):
        return len(str(abs(value)).strip('0'))

    @staticmethod
    def __get_sigfigs_for_decimal(value):
        value_str = str(abs(value))
        decimal_point_index = len(value_str.split('.')[0])
        for i in range(len(value_str)):
            if value_str[i].isdigit():
                if value_str[i] != '0':
                    return len(value_str) - i - (1 if i < decimal_point_index else 0)
        return 0
