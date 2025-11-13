from board import Board
from display import Display
from player import Player
from cpu_player import CPUPlayer
from gamelogic import Gamelogic

# 1. モード選択（game_mode を決める）
print("モードを選んでください")
game_mode = input("1: 人間 vs 人間, 2: 人間 vs CPU を入力: ")

# 2. `players` 辞書（道具箱）の準備
if game_mode == "1":
    # (人間 vs 人間 が選ばれた場合の設定)
    print("人間 vs 人間 モード")
    players = {
        -1: Player(),  # 黒(-1)の担当は、人間の部品
        1: Player()    # 白(1)の担当も、人間の部品
    }
elif game_mode == "2":
    # (人間 vs CPU が選ばれた場合の設定)
    print("人間 vs CPU モード")
    # 2a. CPUレベル選択
    level = input("CPUのレベルを選んでください (1: ランダム, 2: 賢いAI): ")
    # 2b. 先行・後攻 選択
    human_color_str = input("あなたの色を選んでください (B=黒, W=白): ")
    
    if human_color_str.upper() == "B":
        human_color = -1
        cpu_color = 1
    else:
        human_color = 1
        cpu_color = -1
        
    # 2c. 辞書を準備
    players = {
        human_color: Player(),
        cpu_color: CPUPlayer(player_color=cpu_color, level=level)
    }


my_board = Board()
my_display = Display()
my_logic = Gamelogic()
current_player = -1

while True:

    my_display.display_board(my_board)
    counts = my_board.count_stones() ##（石の数を数える)
    my_display.display_info(current_player, counts)
    valid_moves = my_logic.find_all_valid_moves(my_board, current_player)
    # current_player（例：黒 -1）が置ける場所が0個だった場合
    if len(valid_moves) == 0:
        
        # 1. 最初のパスを知らせる
        print(f"{current_player} はパスします!!")
        
        # 2. 「次の人」を計算する
        next_player = -current_player #（例：白 1）
        
        # 3. 「次の人」の動きを「先読み」する
        next_moves = my_logic.find_all_valid_moves(my_board, next_player)
        
        # 4. 【重要】「次の人」のリストの長さをチェックする
        if len(next_moves) == 0:
            # 「次の人」も置けなかった（両者パス）
            print(f"{next_player} もパスします!!")
            break # ゲーム終了
        else:
            # 「次の人」は置けるので、ターンを交代して続ける
            current_player = next_player
            continue
        
        
    current_player_object = players[current_player]
    row, col = current_player_object.get_player_input(my_board, valid_moves, my_logic)
    if  (row, col) not in valid_moves:
        print("そこにはおけません!!")
        continue
    my_logic.make_move(my_board, current_player, row, col)
    if my_logic.check_game_over(my_board, -1, 1) == True:
        break
    current_player = -1 * current_player
counts = my_board.count_stones()
my_display.display_game_over(counts)

