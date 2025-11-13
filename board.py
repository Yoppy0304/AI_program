class Board:  # ← クラス（設計図）を定義

    def __init__(self):  # 盤面の初期化
        # 「実体（インスタンス）」が作られた瞬間に
        # やってほしい初期設定を、ここに書く
        self.size = 8
        grid_data = []
        i = 0 
        for i in range(self.size):# 行
            new_row = []
            for j in range(self.size): #列
                new_row.append(0)

            grid_data.append(new_row)    
        self.grid = grid_data
        self.grid[3][3] = 1
        self.grid[3][4] = -1
        self.grid[4][3] = -1
        self.grid[4][4] = 1
    
    def count_stones(self): ##石の数を数える
        black_count = 0
        white_count = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == -1:
                    black_count = black_count + 1

                elif self.grid[i][j] == 1:
                    white_count = white_count + 1

                elif self.grid[i][j] == 0:
                    pass
                else :
                   print("エラーが発生しました!!")

        return white_count , black_count
    
    def copy(self):
        new_board = Board()
        new_board.size = self.size
        # 盤面データ（grid）を1行ずつコピーする（重要）
        new_board.grid = []
        for row in self.grid:
            new_board.grid.append(row.copy())

        return new_board
                

             
    

    def some_other_method(self):
        # 他に必要なメソッド（機能）...
        pass