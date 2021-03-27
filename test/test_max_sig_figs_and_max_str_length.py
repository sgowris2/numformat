import unittest

from sigfig import SigFig


class TestMaxSigFigsAndMaxStrLength(unittest.TestCase):

    def test_invalid_max_str_length(self):
        with self.assertRaises(ValueError):
            SigFig.sfformat(10.0, max_sig_figs=2, max_length=1)

    def test_zeros(self):
        self.assertEqual('0.0', SigFig.sfformat(0.0, max_sig_figs=2, max_length=3))
        self.assertEqual('0.0', SigFig.sfformat(0.000, max_sig_figs=2, max_length=3))
        self.assertEqual('0.0', SigFig.sfformat(0.000, max_sig_figs=4, max_length=4))
        self.assertEqual('0.000', SigFig.sfformat('0.000', max_sig_figs=2, max_length=5))
        self.assertEqual('0.000', SigFig.sfformat('0.000', max_sig_figs=4, max_length=4))

    def test_integers(self):
        # Positive integers
        self.assertEqual('1', SigFig.sfformat(1, max_sig_figs=2, max_length=3))
        self.assertEqual('2', SigFig.sfformat(2, max_sig_figs=2, max_length=3))
        self.assertEqual('13', SigFig.sfformat(13, max_sig_figs=3, max_length=3))
        self.assertEqual('1000', SigFig.sfformat(1000, max_sig_figs=2, max_length=3))
        self.assertEqual('4.59e+08', SigFig.sfformat(459284756, max_sig_figs=18, max_length=8))

        # Negative integers
        self.assertEqual('-1', SigFig.sfformat(-1, max_sig_figs=2, max_length=3))
        self.assertEqual('-2', SigFig.sfformat(-2, max_sig_figs=2, max_length=3))
        self.assertEqual('-13', SigFig.sfformat(-13, max_sig_figs=3, max_length=3))
        self.assertEqual('-1000', SigFig.sfformat(-1000, max_sig_figs=2, max_length=3))
        self.assertEqual('-4.6e+08', SigFig.sfformat(-459284756, max_sig_figs=18, max_length=8))

    def test_floats(self):
        # Positive floats
        self.assertEqual('0.0032', SigFig.sfformat(0.0032, max_sig_figs=3, max_length=6))
        self.assertEqual('3e-3', SigFig.sfformat(0.0032, max_sig_figs=3, max_length=5))
        self.assertEqual('145.89', SigFig.sfformat(145.89, max_sig_figs=6, max_length=6))
        self.assertEqual('1.30e+06', SigFig.sfformat(1300001.0, max_sig_figs=10, max_length=7))
        self.assertEqual('12700', SigFig.sfformat(12700.00, max_sig_figs=4, max_length=6))
        self.assertEqual('12700.0', SigFig.sfformat(12700.00, max_sig_figs=8, max_length=8))

        # Negative floats
        self.assertEqual('-0.0032', SigFig.sfformat(-0.0032, max_sig_figs=3, max_length=7))
        self.assertEqual('-145.89', SigFig.sfformat(-145.89, max_sig_figs=6, max_length=7))
        self.assertEqual('-1.30e+06', SigFig.sfformat(-1300001.0, max_sig_figs=10, max_length=8))
        self.assertEqual('-12700', SigFig.sfformat(-12700.00, max_sig_figs=4, max_length=6))
        self.assertEqual('-12700.0', SigFig.sfformat(-12700.00, max_sig_figs=8, max_length=8))
    
    def test_strings_max_sig_figs_greater_than_actual_sig_figs(self):
        # Positive integers
        self.assertEqual('1', SigFig.sfformat('1', max_sig_figs=2, max_length=3))
        self.assertEqual('2', SigFig.sfformat('2', max_sig_figs=2, max_length=3))
        self.assertEqual('13', SigFig.sfformat('13', max_sig_figs=3, max_length=3))
        self.assertEqual('1000', SigFig.sfformat('1000', max_sig_figs=2, max_length=3))
        self.assertEqual('4.59e+08', SigFig.sfformat('459284756', max_sig_figs=18, max_length=8))

        # Negative integers
        self.assertEqual('-1', SigFig.sfformat('-1', max_sig_figs=2, max_length=3))
        self.assertEqual('-2', SigFig.sfformat('-2', max_sig_figs=2, max_length=3))
        self.assertEqual('-13', SigFig.sfformat('-13', max_sig_figs=3, max_length=3))
        self.assertEqual('-1000', SigFig.sfformat('-1000', max_sig_figs=2, max_length=3))
        self.assertEqual('-4.6e+08', SigFig.sfformat('-459284756', max_sig_figs=18, max_length=8))

        # Positive floats
        self.assertEqual('0.0032', SigFig.sfformat('0.0032', max_sig_figs=3, max_length=6))
        self.assertEqual('3e-3', SigFig.sfformat('0.0032', max_sig_figs=3, max_length=5))
        self.assertEqual('145.89', SigFig.sfformat('145.89', max_sig_figs=6, max_length=6))
        self.assertEqual('1.30e+06', SigFig.sfformat('1300001.0', max_sig_figs=10, max_length=7))
        self.assertEqual('12700', SigFig.sfformat('12700.00', max_sig_figs=4, max_length=6))
        self.assertEqual('12700.00', SigFig.sfformat('12700.00', max_sig_figs=8, max_length=8))

        # Negative floats
        self.assertEqual('-0.0032', SigFig.sfformat('-0.0032', max_sig_figs=3, max_length=7))
        self.assertEqual('-145.89', SigFig.sfformat('-145.89', max_sig_figs=6, max_length=7))
        self.assertEqual('-1.30e+06', SigFig.sfformat('-1300001.0', max_sig_figs=10, max_length=8))
        self.assertEqual('-12700', SigFig.sfformat('-12700.00', max_sig_figs=4, max_length=6))
        self.assertEqual('-1.27e+04', SigFig.sfformat('-12700.00', max_sig_figs=8, max_length=8))
