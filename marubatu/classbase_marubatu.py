#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 参考源
# https://qiita.com/r34b26/items/317cc82568845d6bbbcb


class Marubatu:
    """oxゲームをまとめたクラス
    """
    def __init__(self):
        self.candidates_text = """
        1|2|3
        -----
        4|5|6
        -----
        7|8|9
        """

        self.coordinate_list = [
            str(i) for i in range(1, 10)
        ]
        self.candidates = [
            2**i for i in range(9)
        ]

        self.pre_user_operations = []
        self.pos_user_operations = []

        self.turn_user = 0
        self.turn_count = 0
        self.err_message = '正しい座標を入力する必要があります。'

    def game_start(self):
        """oxゲームの処理を開始する
        """
        print('座標リスト\n')
        print(self.candidates_text)

        pre_user_input = str()
        pos_user_input = str()

        while True:
            if self.turn_user == 0:
                try:
                    mes = 'pre_userの座標を入力'
                    pre_user_input = input(mes)
                except Exception as e:
                    print(self.err_message)
                    continue

                if pre_user_input in self.coordinate_list:
                    pre_user_operations = self.pre_user_operations
                    self.pre_user_operations = self.operation(
                        pre_user_operations,
                        pre_user_input,
                        'o'
                    )
                    if self.check_decision(self.pre_user_operations):
                        print('user0の勝ち')
                        break

                else:
                    print(self.err_message)
                    continue

                self.turn_user = 1
                self.turn_count += 1

            else:
                try:
                    mes = 'pos_userの座標を入力'
                    pos_user_input = input(mes)
                except Exception as e:
                    print(self.err_message)
                    continue

                if pos_user_input in self.coordinate_list:
                    pos_user_operations = self.pos_user_operations
                    self.pos_user_operations = self.operation(
                        pos_user_operations,
                        pos_user_input,
                        'x'
                    )
                    if self.check_decision(self.pos_user_operations):
                        print('user1の勝ち')
                        break

                else:
                    print(self.err_message)
                    continue
                self.turn_user = 0
                self.turn_count += 1

            if self.turn_count == 9:
                print("引き分けです")
                break

    def operation(
        self,
        user_operations: list,
        user_input: str,
        mark: str
    ):
        """入れ替え操作などを行う

        Args:
            user_operations (list): userが今まで選択位置のリスト
            user_input (str): userの入力値
            mark (str): userの記号

        Returns:
            list: userが選択した位置を加えたuser_operations
        """
        self.candidates_text = self.candidates_text.replace(
            str(user_input),
            mark
        )
        idx = self.coordinate_list.index(user_input)
        self.coordinate_list[idx] = mark
        # self.coordinate_list.remove(user_input)

        user_operations.append(self.candidates[idx])
        print(self.candidates_text)
        return user_operations

    def check_decision(self, coordinate_map: list):
        """勝利判定を行う

        Args:
            coordinate_map (list): 現在選択している位置のリスト

        Returns:
            bool: 勝利ならTrue, それ以外ならFalse
        """
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

        # リスト内を全て足して、decision_coordinates内に
        # total_valがあるかを判定する
        # 判定処理
        total_val = sum([int(i) for i in coordinate_map])
        if total_val in decision_coordinates:
            return True
        return False


marubatu = Marubatu()
marubatu.game_start()
