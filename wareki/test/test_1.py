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
            month = 5
            day = 1

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
        # print(heisei_start.year)
        # print(reiwa_start.year)
        for year in range(int(heisei_start.year), int(reiwa_start.year)+1):
            month = 4
            day = 1

            wareki = convert_to_wareki(year, month, day)
            wareki_str = '平成' + str(year-(int(heisei_start.year)-1)) + '年'
            if (year-(int(heisei_start.year)-1)) is 1:
                wareki_str = '平成元年'
            self.assertEqual(wareki, wareki_str)

    def test_showa(self):
        """test method for showa of convert_to_wareki
        """
        year = 2019
        month = 4
        day = 30
        wareki = convert_to_wareki(year, month, day)
        wareki_str = '平成31年'
        self.assertEqual(wareki, wareki_str)

    def test_other(self):
        """test method for other of convert_to_wareki
        """
        year = 2019
        month = 4
        day = 30
        wareki = convert_to_wareki(year, month, day)
        wareki_str = '平成31年'
        self.assertEqual(wareki, wareki_str)

    # print('西暦2020年4月1日は、', convert_to_wareki(2020, 4, 1), sep='')
    # print('西暦2019年5月1日は、', convert_to_wareki(2019, 5, 1), sep='')
    # print('西暦2019年4月30日は、', convert_to_wareki(2019, 4, 30), sep='')
    # print('西暦1989年1月8日は、', convert_to_wareki(1989, 1, 8), sep='')
    # print('西暦1989年1月7日は、', convert_to_wareki(1989, 1, 7), sep='')
    # print('西暦1974年5月5日は、', convert_to_wareki(1974, 5, 5), sep='')
    # print('西暦1926年12月25日は、', convert_to_wareki(1926, 12, 25), sep='')
    # print('西暦1926年12月24日は、', convert_to_wareki(1926, 12, 24), sep='')


class TestFailedWareki(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
