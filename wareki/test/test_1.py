# coding: utf-8
import unittest
import os
import sys
from datetime import datetime

sys.path.append(os.pardir)
from wareki import convert_to_wareki


class TestSuccessWareki(unittest.TestCase):
    """test class of wareki.py
    """

    def setUp(self):
        """ setUp
        """
        self.wareki_dict = {
            '令和': datetime(2019, 5, 1),
            '平成': datetime(1989, 1, 8),
            '昭和': datetime(1926, 12, 25)
        }

    def test_reiwa(self):
        """test method for reiwa of convert_to_wareki
        """
        reiwa_start = self.wareki_dict['令和']
        for year in range(int(reiwa_start.year), 2030):
            month = reiwa_start.month
            day = reiwa_start.day

            wareki = convert_to_wareki(year, month, day)
            wareki_str = '令和' + str(year-2018) + '年'
            if (year-2018) is 1:
                wareki_str = '令和元年'
            self.assertEqual(wareki, wareki_str)

    def test_heisei(self):
        """test method for heisei of convert_to_wareki
        """
        heisei_start = self.wareki_dict['平成']
        reiwa_start = self.wareki_dict['令和']
        for year in range(int(heisei_start.year), int(reiwa_start.year)+1):
            month = heisei_start.month
            day = heisei_start.day

            wareki = convert_to_wareki(year, month, day)
            wareki_str = '平成' + str(year-(int(heisei_start.year)-1)) + '年'
            if (year-(int(heisei_start.year)-1)) is 1:
                wareki_str = '平成元年'
            self.assertEqual(wareki, wareki_str)

    def test_showa(self):
        """test method for showa of convert_to_wareki
        """
        showa_start = self.wareki_dict['昭和']
        heisei_start = self.wareki_dict['平成']
        for year in range(int(showa_start.year), int(heisei_start.year)):
            month = showa_start.month
            day = showa_start.day

            wareki = convert_to_wareki(year, month, day)
            wareki_str = '昭和' + str(year-(int(showa_start.year)-1)) + '年'
            if (year-(int(showa_start.year)-1)) is 1:
                wareki_str = '昭和元年'
            self.assertEqual(wareki, wareki_str)

    def test_other(self):
        """test method for other of convert_to_wareki
        """
        showa_start = self.wareki_dict['昭和']
        for year in range(
            showa_start.year-1,
            showa_start.year - int(str(showa_start.year)[2:])-1,
            -1
        ):
            month = showa_start.month
            day = showa_start.day
            wareki = convert_to_wareki(year, month, day)
            self.assertEqual(wareki, "昭和以前")


class TestFailedWareki(unittest.TestCase):

    def test_out_of_range_month(self):
        """
        """
        year = 2019
        day = 1
        start_month = 13
        for month in range(start_month, 20):
            with self.assertRaises(ValueError) as er:
                convert_to_wareki(year, month, day)

        self.assertIsInstance(er.exception, ValueError)
        self.assertEqual(er.exception.args[0], 'month must be in 1..12')

    def test_out_of_range_day(self):
        """
        """
        year = 2019
        for month in range(1, 13):
            for day in range(32, 50):
                with self.assertRaises(ValueError) as er:
                    convert_to_wareki(year, month, day)

                err_mes = 'day is out of range for month'
                self.assertIsInstance(er.exception, ValueError)
                self.assertEqual(er.exception.args[0], err_mes)


if __name__ == "__main__":
    unittest.main()
