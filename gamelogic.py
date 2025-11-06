from board import Board

class Gamelogic:
     def __init__(self): ##８方向の設定
        self.directions = [( -1 , -1) , ( 0 , -1) , ( +1 , -1 ),
                           ( -1 , 0 ) , (+1 , 0 ),
                           ( -1 , +1) , ( 0 , +1) , ( +1 , +1)]
        
     def is_valid_move(self, board, player, x, y):##特定のマスに置けるか判定
        if board.grid[x][y] != 0:
          return False
        
        opponent = -1 * player ##自分と相手の色の判定

        for dr, dc in self.directions:
           current_x = x + dr
           current_y = y + dc
           if (current_x < 0 or current_x >7) or (current_y < 0 or current_y > 7):##枠外じゃないかのチェック
                continue ##次に進める
           if board.grid[current_x][current_y] != opponent :
                continue ##次に進める
           while True:
               current_x = current_x + dr
               current_y = current_y + dc
               if (current_x < 0 or current_x >7) or (current_y < 0 or current_y > 7):##枠外じゃないかのチェック
                    break ##ループを中断する
               if board.grid[current_x][current_y] == 0: ##空いたマスがあるかチェック
                    break ##ループを中断する
               if board.grid[current_x][current_y] == player: ##挟めてる場合
                    return True
               if board.grid[current_x][current_y] == opponent: ##挟めてない場合
                    pass
        return False
     
     def find_all_valid_moves(self, board, player): ##置ける場所を全部探す
        valid_moves = [] ##からのリスト作成
        for i in range(board.size):# 行
            for j in range(board.size): #列
                if self.is_valid_move(board, player, i, j) == True:
                    valid_moves.append((i , j))
        return valid_moves
     
     def make_move(self, board, player, x, y): ##石を置き、ひっくり返す
        board.grid[x][y] = player
        opponent = -player
        for dr, dc in self.directions:
            stones_to_change = []
            current_x = x + dr
            current_y = y + dc
            while ((current_x >= 0 and current_x <= 7) and (current_y >= 0 and current_y <= 7)) and board.grid[current_x][current_y] == opponent:
                stones_to_change.append((current_x,current_y))
                current_x = current_x + dr
                current_y = current_y + dc
            if stones_to_change != [] and ((current_x >= 0 and current_x <= 7) and (current_y >= 0 and current_y <= 7)) and board.grid[current_x][current_y] == player:
                for change_x, change_y in stones_to_change:
                    board.grid[change_x][change_y] = player

     def check_game_over(self, board, player1, player2):
         white_count, black_count = board.count_stones()
         if white_count + black_count == 64:
             return True
         moves_for_black = self.find_all_valid_moves(board, player1)
         moves_for_white = self.find_all_valid_moves(board, player2)
         if len(moves_for_black) == 0 and len(moves_for_white) == 0:
             return True
         
         return False

        
         
               
               
           
           
           
           
