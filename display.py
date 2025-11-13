from board import Board




class Display:  # ← クラス（設計図）を定義
     
    def display_board(self, board): ##盤面を表示する
        print( 0,1,2,3,4,5,6,7,8)
        for i in range(board.size):# 行
            print(i+1, end=" ")
            for j in range(board.size): #列
                if board.grid[i][j] == 1:
                    print("W", end=" ")
                elif board.grid[i][j]  == -1:
                    print("B", end=" ")
                elif board.grid[i][j] == 0:
                    print("…", end=" ")
                else:
                    print("エラーが発生しました!!")
            print()

    def display_info(self, player, stone_counts): ##スコア・ターンを表示する
        white_count, black_count = stone_counts
        player_name = ""
        if player == 1:
            player_name = "白"
        elif player == -1:
            player_name = "黒"
        else:
            print("エラーが発生しました!!")

        print(f"スコア: 黒 {black_count} 対 白 {white_count}")
        print(f"現在のターン: {player_name} の番です")

    def display_game_over(self, stone_counts): ##終了結果を表示するz
        white_count, black_count = stone_counts
        print(f"最終結果: 黒 {black_count} 対 白 {white_count}")
        if black_count > white_count:
            print("黒の勝ち!!")

        elif black_count < white_count :
            print("白の勝ち!!")
        elif black_count == white_count :
            print("引き分け")
        else: 
         print("エラーが発生しました")

        
