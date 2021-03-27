from decimal import Decimal
from math import floor, log10


class SigFig:

    @staticmethod
    def sfformat(value,
                 max_sig_figs: int = None,
                 max_length: int = None,
                 allow_scientific_notation: bool = True):

        SigFig.__check_sfformat_args(max_sig_figs=max_sig_figs,
                                     max_length=max_length,
                                     allow_scientific_notation=allow_scientific_notation)

        value = SigFig.__convert_to_numeric(value)

        sig_figs = SigFig.__get_sigfigs(value)

        value, value_str, new_sig_figs = SigFig.__convert_to_desired_sigfigs_str(max_sig_figs, sig_figs, value)

        if SigFig.__is_zero(value):
            return value_str

        value_str = SigFig.__convert_to_desired_length_str(value, value_str, new_sig_figs, max_length,
                                                           allow_scientific_notation)

        return value_str

    # Private Methods

    @staticmethod
    def __convert_to_desired_sigfigs_str(desired_sig_figs, sig_figs, value):
        if desired_sig_figs is not None:
            if desired_sig_figs >= sig_figs:
                return value, str(value), sig_figs
            else:
                order = SigFig.__get_order(value)
                value = round(value, desired_sig_figs - order)
                if (value % 1) == 0:
                    value = int(value)
                return value, str(value), desired_sig_figs
        return value, str(value), sig_figs

    @staticmethod
    def __convert_to_desired_length_str(value, value_str, sig_figs, max_length, allow_scientific_notation):

        if max_length is not None:
            if len(value_str) <= max_length:
                return value_str
            elif allow_scientific_notation:
                value_str = SigFig.__convert_to_scientific_notation_str(max_length, sig_figs, value, value_str)
        return value_str

    @staticmethod
    def __convert_to_scientific_notation_str(max_length, sig_figs, value, value_str):

        def _sn_format(sig_figs, value):
            sn_format = '{{:.{}e}}'.format(sig_figs - 1)
            sn_value_str = sn_format.format(value)
            return sn_value_str

        sn_value_str = _sn_format(sig_figs, value)
        if max_length >= len(sn_value_str):
            return sn_value_str
        else:
            digit_difference = len(sn_value_str) - max_length
            if digit_difference < sig_figs:
                desired_sig_figs = sig_figs - digit_difference
                value, value_str, new_sig_figs = SigFig.__convert_to_desired_sigfigs_str(desired_sig_figs, sig_figs,
                                                                                         value)
                return _sn_format(new_sig_figs, value)
        return value_str

    @staticmethod
    def __get_sigfigs(value):

        if isinstance(value, int):
            return SigFig.__get_sigfigs_for_integer(value)
        if isinstance(value, Decimal):
            return SigFig.__get_sigfigs_for_decimal(value)

        raise ValueError('Could not find sigfigs for input - {}'.format(value))

    @staticmethod
    def __get_order(value):
        if isinstance(value, Decimal) and value.is_zero():
            return 0
        elif isinstance(value, int) and value == 0:
            return 0
        order = floor(log10(abs(value))) + 1
        return order

    @staticmethod
    def __convert_to_numeric(value):
        if isinstance(value, int):
            return value
        elif isinstance(value, float):
            return SigFig.__to_decimal(repr(value))
        elif isinstance(value, str):
            if '.' not in value:
                return SigFig.__to_int(value)
            return SigFig.__to_decimal(value)
        else:
            raise ValueError('Input was not in any of the supported formats '
                             'int, float, decimal.Decimal. Received object of type {}'.format(type(value)))

    @staticmethod
    def __check_sfformat_args(max_sig_figs: int = None,
                              max_length: int = None,
                              allow_scientific_notation: bool = True):
        if max_sig_figs is not None and max_sig_figs < 1:
            raise ValueError('\'max_sig_figs\' must be >= 1. Received {}'.format(max_sig_figs))
        if max_length is not None and max_length < 3:
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
    def __to_int(value):
        try:
            value = int(value)
        except:
            raise ValueError('Input is not a valid number - {}'.format(value))
        return value

    @staticmethod
    def __is_zero(value):
        if isinstance(value, int):
            return value == 0
        elif isinstance(value, Decimal):
            return value.is_zero()
        else:
            return False

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
