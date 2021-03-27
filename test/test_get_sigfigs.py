import unittest
from sigfig import SigFig


class TestGetSigFigs(unittest.TestCase):

    def test_zeros(self):
        self.assertEqual(0, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric(0)))
        self.assertEqual(0, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric(0.0)))
        self.assertEqual(0, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric(0.000)))

    def test_positive_int(self):
        self.assertEqual(1, SigFig._SigFig__get_sigfigs(1))
        self.assertEqual(1, SigFig._SigFig__get_sigfigs(2))
        self.assertEqual(2, SigFig._SigFig__get_sigfigs(13))
        self.assertEqual(1, SigFig._SigFig__get_sigfigs(1000))
        self.assertEqual(9, SigFig._SigFig__get_sigfigs(459284756))

    def test_negative_int(self):
        self.assertEqual(1, SigFig._SigFig__get_sigfigs(-1))
        self.assertEqual(1, SigFig._SigFig__get_sigfigs(-2))
        self.assertEqual(2, SigFig._SigFig__get_sigfigs(-13))
        self.assertEqual(1, SigFig._SigFig__get_sigfigs(-1000))
        self.assertEqual(9, SigFig._SigFig__get_sigfigs(-459284756))

    def test_positive_float(self):
        self.assertEqual(4, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric(27.36)))
        self.assertEqual(2, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric(0.0032)))
        self.assertEqual(5, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric(1270.000)))
        self.assertEqual(7, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric(12000.01)))

    def test_negative_float(self):
        self.assertEqual(4, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric(-27.36)))
        self.assertEqual(2, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric(-0.0032)))
        self.assertEqual(5, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric(-1270.000)))
        self.assertEqual(7, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric(-12000.01)))

    def test_string(self):
        self.assertEqual(0, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('0')))
        self.assertEqual(0, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('0.0')))
        self.assertEqual(0, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('0.000')))
        self.assertEqual(1, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('1')))
        self.assertEqual(1, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('2')))
        self.assertEqual(2, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('13')))
        self.assertEqual(1, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('1000')))
        self.assertEqual(9, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('459284756')))
        self.assertEqual(1, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('-1')))
        self.assertEqual(1, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('-2')))
        self.assertEqual(2, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('-13')))
        self.assertEqual(1, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('-1000')))
        self.assertEqual(9, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('-459284756')))
        self.assertEqual(4, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('27.36')))
        self.assertEqual(2, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('0.0032')))
        self.assertEqual(7, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('1270.000')))
        self.assertEqual(7, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('12000.01')))
        self.assertEqual(4, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('-27.36')))
        self.assertEqual(2, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('-0.0032')))
        self.assertEqual(7, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('-1270.000')))
        self.assertEqual(7, SigFig._SigFig__get_sigfigs(SigFig._SigFig__convert_to_numeric('-12000.01')))