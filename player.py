

class Player:# ← クラス（設計図）を定義
    def get_player_input(self, board, valid_moves, logic): ##キーボード入力を受け取る
        while True:
            try:
                print("どこにおく？（(3,5)のように'列,行'で入力")
                a = input()
                b = a.split(",")

                row_num = int(b[0]) - 1
                col_num = int(b[1]) - 1
                return row_num , col_num
            except:
                print("入力が間違ってます！！")



