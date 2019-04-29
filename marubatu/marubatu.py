#!/usr/bin/env python
# -*- coding:utf-8 -*-
from random import shuffle
# import time

# 勝敗がついているかチェック
# def checker(map):
# 　　
# 　　#ビットで勝敗判定
# 　　for check in check_ary:
# 　　　　if ((check & map) == check):
# 　　　　　　return True
# 　　return False


print('以下の数字で座標を指定してください')
text = """
1|2|3
-----
4|5|6
-----
7|8|9
"""
print(text)


def check_decision(coordinate_map):

    # candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    candidates = [2**i for i in range(9)]
    decision_coordinates = []

    for i in range(3):
        # 横の合計を求める
        yoko_first_idx = i*3
        yoko_last_idx = (i+1)*3

        yoko_ans = sum(candidates[yoko_first_idx:yoko_last_idx])
        decision_coordinates.append(yoko_ans)

        # 縦の合計を求める
        tate_list = [candidates[i+3*j] for j in range(3)]
        tate_ans = sum(tate_list)
        decision_coordinates.append(tate_ans)

    # 斜め
    # 1+16+256=273
    # 4+16+64=84

    # 斜め 1
    # 1+16+256=273
    naname_1_list = [candidates[4*i] for i in range(3)]
    naname_1_ans = sum(naname_1_list)
    decision_coordinates.append(naname_1_ans)

    # 斜め 2
    # 4+16+64=84
    naname_2_list = [candidates[2*(i+1)] for i in range(3)]
    naname_2_ans = sum(naname_2_list)
    decision_coordinates.append(naname_2_ans)

    # 横列
    # 1+2+4=7
    # 8+16+32=56
    # 64+128+256=448

    # 縦列
    # 1+8+64=73
    # 2+16+128=146
    # 4+32+256=292

    # 斜め
    # 1+16+256=273
    # 4+16+64=84

    print(decision_coordinates)
    print(coordinate_map)

    total_val = sum([int(i) for i in coordinate_map])
    if total_val in decision_coordinates:
        return True
    return False


def marubatu_game():

    coordinate_list = [str(i) for i in range(1, 10)]
    candidates = [2**i for i in range(9)]

    print('candidates : ')
    print(candidates)

    print(coordinate_list)

    pre_user_input = str()
    pre_user_operations = []

    pos_user_input = str()
    pos_user_operations = []

    err_message = '正しい座標を入力する必要があります。'

    turn_user = 0
    while True:
        if turn_user == 0:
            try:
                text = 'pre_userの座標を入力'
                pre_user_input = input(text)
            except Exception as e:
                print(err_message)
                continue

            print('test: ', pre_user_input, type(pre_user_input))
            if pre_user_input in coordinate_list:
                print(pre_user_input)
                text = text.replace(str(pre_user_input), "o")

                idx = coordinate_list.index(pre_user_input)
                coordinate_list.remove(pre_user_input)

                print(candidates[idx])
                # pre_user_operations.append(pre_user_input)
                pre_user_operations.append(candidates[idx])

            else:
                print(err_message)
                continue
            turn_user = 1

        else:
            try:
                text = 'pos_userの座標を入力'
                pos_user_input = input(text)
            except Exception as e:
                print(err_message)
                continue

            print('test: ', pos_user_input, type(pos_user_input))
            if pos_user_input in coordinate_list:
                print(pos_user_input)
                text = text.replace(str(pos_user_input), "x")

                idx = coordinate_list.index(pos_user_input)
                coordinate_list.remove(pos_user_input)

                print(candidates[idx])
                # pre_user_operations.append(pre_user_input)
                pos_user_operations.append(candidates[idx])

            else:
                print(err_message)
                continue
            turn_user = 0


# marubatu_game()

# # candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
candidates = [2**i for i in range(9)]
# decision_coordinates = []

# for i in range(3):
#     # 横の合計を求める
#     yoko_first_idx = i*3
#     yoko_last_idx = (i+1)*3

#     yoko_ans = sum(candidates[yoko_first_idx:yoko_last_idx])
#     decision_coordinates.append(yoko_ans)

#     # 縦の合計を求める
#     tate_list = [candidates[i+3*j] for j in range(3)]
#     tate_ans = sum(tate_list)
#     decision_coordinates.append(tate_ans)

# # 斜め
# # 1+16+256=273
# # 4+16+64=84
;
# 斜め 1
# 1+16+256=273
naname_1_list = [candidates[4*i] for i in range(3)]
naname_1_ans = sum(naname_1_list)
# decision_coordinates.append(naname_1_ans)


# 斜め 2
# 4+16+64=84
naname_2_list = [candidates[2*(i+1)] for i in range(3)]
naname_2_ans = sum(naname_2_list)
# decision_coordinates.append(naname_2_ans)

# print(decision_coordinates)

print(check_decision(naname_1_list))
