from board import Board
from display import Display
from player import Player
from gamelogic import Gamelogic


my_board = Board()
my_display = Display()
my_player = Player()
my_logic = Gamelogic()
current_player = -1

while True:

    my_display.display_board(my_board)
    counts = my_board.count_stones() ##（石の数を数える)
    my_display.display_info(current_player, counts)
    valid_moves = my_logic.find_all_valid_moves(my_board, current_player)
    if len(valid_moves) == 0:
        print(f"{current_player} はパスします!!")
        # 1. 【重要】交代した「相手」も置ける場所があるか、すぐにチェックする
        next_valid_moves = my_logic.find_all_valid_moves(my_board, current_player)
        # 2. もし「相手」も置ける場所が0個だったら...
        if len(next_valid_moves) == 0:
            print(f"{current_player} もパスします!!")
            # 両者パスなので、ゲーム終了！
            break 
        
        # 3 （相手は置ける場所があったので）
        #    パスした人のターンだけをスキップする
        continue
    row, col = my_player.get_player_input()
    if  (row, col) not in valid_moves:
        print("そこにはおけません!!")
        continue
    my_logic.make_move(my_board, current_player, row, col)
    if my_logic.check_game_over(my_board, -1, 1) == True:
        break
    current_player = -1 * current_player
counts = my_board.count_stones()
my_display.display_game_over(counts)

