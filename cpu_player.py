import random
class CPUPlayer:
        def __init__(self, player_color, level):
                self.color = player_color
                self.level = level
                
        

        def get_player_input(self, board, valid_moves, logic): ##キーボード入力を受け取る
                if self.level == "1":
                    move = self._think_random(valid_moves)
                    return move
                elif self.level == "2":
                       move = self._think_greedy(board, valid_moves, logic) # (賢いAIを呼ぶ)
                       return move
                
                
        def _think_random(self, valid_moves):
                # valid_moves リストから、ランダムに1個の要素を選ぶ
                chosen_move = random.choice(valid_moves)
                return chosen_move
        
        def _think_greedy(self, board, valid_moves, logic):
            best_move = None
            best_score = -1
               
            for move in valid_moves:
                    row, col = move
                    temp_board = board.copy()
                    logic.make_move(temp_board, self.color, row, col)
                    white, black = temp_board.count_stones()
                    my_score = black if self.color == -1 else white
                    if my_score > best_score:
                            best_score = my_score
                            best_move = move
            return best_move
                             
