import random

def create_board(rows, cols):
    """
    rows x cols の盤面を生成し、初期値を格納して返す。
    まだ地雷は配置しない。
    """
    board = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            cell = {
                'mine': False,    # 地雷があるか
                'revealed': False,  # 開いているか
                'flagged': False    # 旗を立てているか
            }
            row.append(cell)
        board.append(row)
    return board

def place_mines(board, rows, cols, mines):
    """
    board 上に mines 個の地雷をランダムに配置する
    """
    total_cells = rows * cols
    mine_positions = random.sample(range(total_cells), mines)  # インデックスをランダム取得

    for pos in mine_positions:
        r = pos // cols
        c = pos % cols
        board[r][c]['mine'] = True

def debug_print_board(board, rows, cols):
    """
    内部データを可視化するデバッグ用関数。
    mine: M / それ以外: .
    """
    print("=== デバッグ用盤面表示 ===")
    for r in range(rows):
        row_str = ""
        for c in range(cols):
            if board[r][c]['mine']:
                row_str += "M "
            else:
                row_str += ". "
        print(row_str)
    print()

def main():
    # ゲームの初期設定
    rows, cols, mines = 9, 9, 10  # 9x9の盤面に10個の地雷
    print(f"{rows} x {cols} の盤面に地雷を {mines} 個配置します。")

    # 盤面の作成
    board = create_board(rows, cols)

    # 地雷を配置
    place_mines(board, rows, cols, mines)
    print("地雷を配置しました。")

    # デバッグ用に盤面を表示
    debug_print_board(board, rows, cols)

if __name__ == "__main__":
    main()

def count_mines_around(board, r, c, rows, cols):
    """
    あるマス(r,c)の周囲8マスにいくつ地雷があるか数える
    """
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if board[nr][nc]['mine']:
                    count += 1
    return count
def debug_print_board(board, rows, cols):
    """
    内部データを可視化するデバッグ用関数。
    mine: M / flagged: F / revealed: R
    """
    for r in range(rows):
        row_str = ""
        for c in range(cols):
            cell = board[r][c]
            if cell['mine']:
                row_str += "M "
            else:
                row_str += ". "
        print(row_str)
    print()

def main():
    rows, cols, mines = 9, 9, 10
    board = create_board(rows, cols)
    place_mines(board, rows, cols, mines)
    debug_print_board(board, rows, cols)

if __name__ == "__main__":
    main()

def get_user_input(rows, cols):
    """
    ユーザーから r, c を入力して返す。
    範囲外の場合は再入力を求める。
    """
    while True:
        user_input = input("行と列をスペース区切りで指定してください (例: 0 0): ")
        try:
            r_str, c_str = user_input.split()
            r = int(r_str)
            c = int(c_str)
            if 0 <= r < rows and 0 <= c < cols:
                return r, c
            else:
                print("範囲外です。再入力してください。")
        except ValueError:
            print("正しい形式で入力してください。")

def main():
    rows, cols, mines = 9, 9, 10
    board = create_board(rows, cols)
    place_mines(board, rows, cols, mines)

    while True:
        debug_print_board(board, rows, cols)
        print("マスを開く座標を指定してください。")
        r, c = get_user_input(rows, cols)
        print(f"選択されたマス: ({r}, {c})")

        # （後で開く処理を実装する）
        # 一旦、入力が永遠に続く状態

if __name__ == "__main__":
    main()

def reveal_cell(board, r, c, rows, cols):
    """
    指定マスを開く処理。
    地雷なら True（ゲームオーバー）を返す。
    それ以外なら False。
    """
    if board[r][c]['mine']:
        board[r][c]['revealed'] = True
        return True  # 地雷を踏んだ
    board[r][c]['revealed'] = True
    return False

def main():
    rows, cols, mines = 9, 9, 10
    board = create_board(rows, cols)
    place_mines(board, rows, cols, mines)

    while True:
        debug_print_board(board, rows, cols)
        print("マスを開く座標を指定してください。")
        r, c = get_user_input(rows, cols)
        
        if reveal_cell(board, r, c, rows, cols):
            print("地雷を踏みました！ゲームオーバー！")
            debug_print_board(board, rows, cols)  # 最後に全体を見せる
            break

def reveal_cell(board, r, c, rows, cols):
    if board[r][c]['mine']:
        board[r][c]['revealed'] = True
        return True  # 地雷踏んだ
    
    # すでに開いてたら何もしない
    if board[r][c]['revealed']:
        return False
    
    board[r][c]['revealed'] = True
    # 周囲の地雷数をチェック
    mine_count = count_mines_around(board, r, c, rows, cols)
    if mine_count == 0:
        # 周囲のマスも開く（再帰or BFS）
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    reveal_cell(board, nr, nc, rows, cols)
    
    return False

def display_board(board, rows, cols):
    """
    ユーザー向けの盤面表示
    """
    print("   ", end="")
    for c in range(cols):
        print(f"{c:2d} ", end="")
    print()

    for r in range(rows):
        print(f"{r:2d} ", end="")
        for c in range(cols):
            cell = board[r][c]
            if cell['revealed']:
                if cell['mine']:
                    print("*  ", end="")  # 地雷
                else:
                    count = count_mines_around(board, r, c, rows, cols)
                    print(f"{count}  ", end="")
            else:
                if cell['flagged']:
                    print("F  ", end="")
                else:
                    print("■ ", end=" ")  # 閉じているマス
        print()
    print()

def main():
    rows, cols, mines = 9, 9, 10
    board = create_board(rows, cols)
    place_mines(board, rows, cols, mines)

    while True:
        display_board(board, rows, cols)
        r, c = get_user_input(rows, cols)
        if reveal_cell(board, r, c, rows, cols):
            print("地雷を踏みました！ゲームオーバー！")
            # 全部開いて終了
            for rr in range(rows):
                for cc in range(cols):
                    board[rr][cc]['revealed'] = True
            display_board(board, rows, cols)
            break

def get_user_action(rows, cols):
    """
    例: "R 2 3" -> (action='R', r=2, c=3)
        "F 5 1" -> (action='F', r=5, c=1)
    """
    while True:
        user_input = input("操作と座標を指定 (例: R 0 0 / F 0 0): ").strip().upper()
        parts = user_input.split()
        if len(parts) != 3:
            print("入力形式が違います。例: R 0 0")
            continue
        action, r_str, c_str = parts
        if action not in ['R', 'F']:
            print("操作は 'R'(reveal) か 'F'(flag) のみです。")
            continue
        try:
            r = int(r_str)
            c = int(c_str)
            if 0 <= r < rows and 0 <= c < cols:
                return action, r, c
            else:
                print("範囲外です。")
        except ValueError:
            print("数字を指定してください。")

def main():
    rows, cols, mines = 9, 9, 10
    board = create_board(rows, cols)
    place_mines(board, rows, cols, mines)

    while True:
        display_board(board, rows, cols)
        action, r, c = get_user_action(rows, cols)

        if action == 'F':
            board[r][c]['flagged'] = not board[r][c]['flagged']
            continue

        # R の場合
        if reveal_cell(board, r, c, rows, cols):
            print("地雷を踏みました！ゲームオーバー！")
            for rr in range(rows):
                for cc in range(cols):
                    board[rr][cc]['revealed'] = True
            display_board(board, rows, cols)
            break

def check_victory(board, rows, cols):
    """
    まだ開かれていない非地雷マスがあれば False を返す。
    """
    for r in range(rows):
        for c in range(cols):
            if not board[r][c]['mine'] and not board[r][c]['revealed']:
                return False
    return True

def main():
    # ...
    while True:
        display_board(board, rows, cols)
        if check_victory(board, rows, cols):
            print("おめでとうございます！すべてのマスを開きました！")
            break
        action, r, c = get_user_action(rows, cols)
        #



