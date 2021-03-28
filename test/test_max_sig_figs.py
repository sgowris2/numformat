import unittest

from sigfig import SigFig


class TestMaxSigFigs(unittest.TestCase):

    def test_zeros(self):
        self.assertEqual('0', SigFig.autoformat(0, max_sig_figs=2))
        self.assertEqual('0.0', SigFig.autoformat(0.0, max_sig_figs=2))
        self.assertEqual('0.0', SigFig.autoformat(0.000, max_sig_figs=2))
        self.assertEqual('0.0', SigFig.autoformat(0.000, max_sig_figs=4))
        self.assertEqual('0.000', SigFig.autoformat('0.000', max_sig_figs=2))
        self.assertEqual('0.000', SigFig.autoformat('0.000', max_sig_figs=4))

    def test_integers_max_sig_figs_greater_than_actual_sig_figs(self):
        # Positive integers
        self.assertEqual('1', SigFig.autoformat(1, max_sig_figs=2))
        self.assertEqual('2', SigFig.autoformat(2, max_sig_figs=2))
        self.assertEqual('13', SigFig.autoformat(13, max_sig_figs=3))
        self.assertEqual('1000', SigFig.autoformat(1000, max_sig_figs=2))
        self.assertEqual('459284756', SigFig.autoformat(459284756, max_sig_figs=18))

        # Negative integers
        self.assertEqual('-1', SigFig.autoformat(-1, max_sig_figs=2))
        self.assertEqual('-2', SigFig.autoformat(-2, max_sig_figs=2))
        self.assertEqual('-13', SigFig.autoformat(-13, max_sig_figs=3))
        self.assertEqual('-1000', SigFig.autoformat(-1000, max_sig_figs=2))
        self.assertEqual('-459284756', SigFig.autoformat(-459284756, max_sig_figs=18))

    def test_integers_max_sig_figs_less_than_actual_sig_figs(self):
        # Positive integers
        self.assertEqual('10', SigFig.autoformat(11, max_sig_figs=1))
        self.assertEqual('30', SigFig.autoformat(29, max_sig_figs=1))
        self.assertEqual('140', SigFig.autoformat(137, max_sig_figs=2))
        self.assertEqual('1000', SigFig.autoformat(1001, max_sig_figs=2))
        self.assertEqual('459000000', SigFig.autoformat(459284756, max_sig_figs=3))

        # Negative integers
        self.assertEqual('-10', SigFig.autoformat(-11, max_sig_figs=1))
        self.assertEqual('-30', SigFig.autoformat(-29, max_sig_figs=1))
        self.assertEqual('-140', SigFig.autoformat(-137, max_sig_figs=2))
        self.assertEqual('-1000', SigFig.autoformat(-1001, max_sig_figs=2))
        self.assertEqual('-459000000', SigFig.autoformat(-459284756, max_sig_figs=3))

    def test_floats_max_sig_figs_greater_than_actual_sig_figs(self):
        # Positive floats
        self.assertEqual('0.0032', SigFig.autoformat(0.0032, max_sig_figs=3))
        self.assertEqual('145.89', SigFig.autoformat(145.89, max_sig_figs=6))
        self.assertEqual('1300001.0', SigFig.autoformat(1300001.0, max_sig_figs=10))
        self.assertEqual('12700', SigFig.autoformat(12700.00, max_sig_figs=4))
        self.assertEqual('12700.0', SigFig.autoformat(12700.00, max_sig_figs=8))

        # Negative floats
        self.assertEqual('-0.0032', SigFig.autoformat(-0.0032, max_sig_figs=3))
        self.assertEqual('-145.89', SigFig.autoformat(-145.89, max_sig_figs=6))
        self.assertEqual('-1300001.0', SigFig.autoformat(-1300001.0, max_sig_figs=10))
        self.assertEqual('-12700', SigFig.autoformat(-12700.00, max_sig_figs=4))
        self.assertEqual('-12700.0', SigFig.autoformat(-12700.00, max_sig_figs=8))

    def test_floats_max_sig_figs_less_than_actual_sig_figs(self):
        # Positive floats
        self.assertEqual('0.003', SigFig.autoformat(0.0032, max_sig_figs=1))
        self.assertEqual('146', SigFig.autoformat(145.89, max_sig_figs=3))
        self.assertEqual('1300000', SigFig.autoformat(1300001.0, max_sig_figs=3))
        self.assertEqual('13000', SigFig.autoformat(12700.00, max_sig_figs=2))

        # Negative floats
        self.assertEqual('-0.003', SigFig.autoformat(-0.0032, max_sig_figs=1))
        self.assertEqual('-146', SigFig.autoformat(-145.89, max_sig_figs=3))
        self.assertEqual('-1300000', SigFig.autoformat(-1300001.0, max_sig_figs=3))
        self.assertEqual('-13000', SigFig.autoformat(-12700.00, max_sig_figs=2))

    def test_strings_max_sig_figs_greater_than_actual_sig_figs(self):
        # Positive integers
        self.assertEqual('1', SigFig.autoformat('1', max_sig_figs=2))
        self.assertEqual('2', SigFig.autoformat('2', max_sig_figs=2))
        self.assertEqual('13', SigFig.autoformat('13', max_sig_figs=3))
        self.assertEqual('1000', SigFig.autoformat('1000', max_sig_figs=2))
        self.assertEqual('459284756', SigFig.autoformat('459284756', max_sig_figs=18))

        # Negative integers
        self.assertEqual('-1', SigFig.autoformat('-1', max_sig_figs=2))
        self.assertEqual('-2', SigFig.autoformat('-2', max_sig_figs=2))
        self.assertEqual('-13', SigFig.autoformat('-13', max_sig_figs=3))
        self.assertEqual('-1000', SigFig.autoformat('-1000', max_sig_figs=2))
        self.assertEqual('-459284756', SigFig.autoformat('-459284756', max_sig_figs=18))

        # Positive floats
        self.assertEqual('0.0032', SigFig.autoformat('0.0032', max_sig_figs=3))
        self.assertEqual('145.89', SigFig.autoformat('145.89', max_sig_figs=6))
        self.assertEqual('1300001.0', SigFig.autoformat('1300001.0', max_sig_figs=10))
        self.assertEqual('12700', SigFig.autoformat('12700.00', max_sig_figs=4))
        self.assertEqual('12700.00', SigFig.autoformat('12700.00', max_sig_figs=8))

        # Negative floats
        self.assertEqual('-0.0032', SigFig.autoformat('-0.0032', max_sig_figs=3))
        self.assertEqual('-145.89', SigFig.autoformat('-145.89', max_sig_figs=6))
        self.assertEqual('-1300001.0', SigFig.autoformat('-1300001.0', max_sig_figs=10))
        self.assertEqual('-12700', SigFig.autoformat('-12700.00', max_sig_figs=4))
        self.assertEqual('-12700.00', SigFig.autoformat('-12700.00', max_sig_figs=8))

    def test_strings_max_sig_figs_less_than_actual_sig_figs(self):
        # Positive integers
        self.assertEqual('10', SigFig.autoformat('11', max_sig_figs=1))
        self.assertEqual('30', SigFig.autoformat('29', max_sig_figs=1))
        self.assertEqual('140', SigFig.autoformat('137', max_sig_figs=2))
        self.assertEqual('1000', SigFig.autoformat('1001', max_sig_figs=2))
        self.assertEqual('459000000', SigFig.autoformat('459284756', max_sig_figs=3))

        # Negative integers
        self.assertEqual('-10', SigFig.autoformat('-11', max_sig_figs=1))
        self.assertEqual('-30', SigFig.autoformat('-29', max_sig_figs=1))
        self.assertEqual('-140', SigFig.autoformat('-137', max_sig_figs=2))
        self.assertEqual('-1000', SigFig.autoformat('-1001', max_sig_figs=2))
        self.assertEqual('-459000000', SigFig.autoformat('-459284756', max_sig_figs=3))

        # Positive floats
        self.assertEqual('0.003', SigFig.autoformat('0.0032', max_sig_figs=1))
        self.assertEqual('146', SigFig.autoformat('145.89', max_sig_figs=3))
        self.assertEqual('1300000', SigFig.autoformat('1300001.0', max_sig_figs=3))
        self.assertEqual('13000', SigFig.autoformat('12700.00', max_sig_figs=2))

        # Negative floats
        self.assertEqual('-0.003', SigFig.autoformat('-0.0032', max_sig_figs=1))
        self.assertEqual('-146', SigFig.autoformat('-145.89', max_sig_figs=3))
        self.assertEqual('-1300000', SigFig.autoformat('-1300001.0', max_sig_figs=3))
        self.assertEqual('-13000', SigFig.autoformat('-12700.00', max_sig_figs=2))
