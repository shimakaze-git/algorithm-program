# coding: utf-8

# 引数 y に西暦の年、 m に月、 d に日を数値で指定します。
# 和暦（元号XX年）を返します。（例. 1974年5月5日は「昭和49年」）
# 昭和開始日以前の日付の場合は、「昭和以前」と返します。
# 各元号の１年は「元年」と返します。（例. 2019年6月１日は「令和元年」）
# 各元号の開始日は辞書 WAREKI_START に格納されています。
# 辞書 WAREKI_START は新しい元号から順番に並んでいます。


from datetime import datetime

WAREKI_START = {
    '令和': datetime(2019, 5, 1),
    '平成': datetime(1989, 1, 8),
    '昭和': datetime(1926, 12, 25)
}


# year = 2019
# print(int(str(year)[2:]))
# print(WAREKI_START)


def convert_to_wareki(y, m, d):
    """西暦の年月日を和暦の年に変換する."""
    try:
        y_m_d = datetime(y, m, d)
        if WAREKI_START['令和'] <= y_m_d:
            reiwa_year = WAREKI_START['令和'].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = '令和'
        elif WAREKI_START['平成'] <= y_m_d:
            reiwa_year = WAREKI_START['平成'].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = '平成'
        elif WAREKI_START['昭和'] <= y_m_d:
            reiwa_year = WAREKI_START['昭和'].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = '昭和'
        else:
            return '昭和以前'

        if year == 1:
            year = '元'

        return era_str + str(year) + '年'
    except ValueError as e:
        raise e


def main():
    print('西暦2020年4月1日は、', convert_to_wareki(2020, 4, 1), sep='')
    print('西暦2019年5月1日は、', convert_to_wareki(2019, 5, 1), sep='')
    print('西暦2019年4月30日は、', convert_to_wareki(2019, 4, 30), sep='')
    print('西暦1989年1月8日は、', convert_to_wareki(1989, 1, 8), sep='')
    print('西暦1989年1月7日は、', convert_to_wareki(1989, 1, 7), sep='')
    print('西暦1974年5月5日は、', convert_to_wareki(1974, 5, 5), sep='')
    print('西暦1926年12月25日は、', convert_to_wareki(1926, 12, 25), sep='')
    print('西暦1926年12月24日は、', convert_to_wareki(1926, 12, 24), sep='')
    print('西暦1989年4月1日は、', convert_to_wareki(1989, 4, 1), sep='')


if __name__ == '__main__':
    main()

# ad_to_ja = lambda year : int(str(year)[2:]) - 18
# print(ad_to_ja(2019))

# https://blog.pyq.jp/entry/Release_190416_converted2019
