import random
from colorama import init, Fore, Style

init(autoreset=True)

def display_board(board, rows, cols):
    # ...
    # 例: 地雷なら赤く表示
    if cell['mine']:
        print(Fore.RED + "*  " + Style.RESET_ALL, end="")
    # ...

def create_board(rows, cols):
    """
    rows x cols の盤面を生成し、初期値を格納して返す。
    まだ地雷は配置しない。
    """
    return [[{'mine': False, 'revealed': False, 'flagged': False} for _ in range(cols)] for _ in range(rows)]

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

def count_mines_around(board, r, c, rows, cols):
    """
    指定マス (r, c) の周囲8マスにいくつ地雷があるか数える
    """
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc]['mine']:
                count += 1
    return count

def reveal_cell(board, r, c, rows, cols):
    """
    指定マスを開く処理。
    地雷なら True（ゲームオーバー）を返す。それ以外なら False。
    """
    if board[r][c]['mine']:
        board[r][c]['revealed'] = True
        return True  # 地雷を踏んだ

    if board[r][c]['revealed']:
        return False  # 既に開かれている場合は何もしない

    board[r][c]['revealed'] = True
    mine_count = count_mines_around(board, r, c, rows, cols)
    if mine_count == 0:
        # 周囲のマスを再帰的に開く
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    reveal_cell(board, nr, nc, rows, cols)

    return False

def display_board(board, rows, cols):
    """
    ユーザー向けの盤面表示
    """
    print("   " + " ".join(f"{c:2}" for c in range(cols)))
    for r in range(rows):
        row_str = f"{r:2} "
        for c in range(cols):
            cell = board[r][c]
            if cell['revealed']:
                if cell['mine']:
                    row_str += "*  "
                else:
                    count = count_mines_around(board, r, c, rows, cols)
                    row_str += f"{count}  "
            else:
                if cell['flagged']:
                    row_str += "F  "
                else:
                    row_str += "■  "
        print(row_str)
    print()

def get_user_action(rows, cols):
    """
    ユーザーの操作を取得する。形式: "R 2 3" または "F 2 3"
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
            r, c = int(r_str), int(c_str)
            if 0 <= r < rows and 0 <= c < cols:
                return action, r, c
            else:
                print("範囲外です。再入力してください。")
        except ValueError:
            print("正しい形式で入力してください。")

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
    # ゲームの初期設定
    rows, cols, mines = 9, 9, 10
    board = create_board(rows, cols)
    place_mines(board, rows, cols, mines)

    while True:
        display_board(board, rows, cols)
        if check_victory(board, rows, cols):
            print("おめでとうございます！すべてのマスを開きました！")
            break

        action, r, c = get_user_action(rows, cols)

        if action == 'F':
            board[r][c]['flagged'] = not board[r][c]['flagged']
        elif action == 'R':
            if reveal_cell(board, r, c, rows, cols):
                print("地雷を踏みました！ゲームオーバー！")
                # 全部開いて終了
                for rr in range(rows):
                    for cc in range(cols):
                        board[rr][cc]['revealed'] = True
                display_board(board, rows, cols)
                break

def display_remaining_mines(board, mines):
    flag_count = 0
    for row in board:
        for cell in row:
            if cell['flagged']:
                flag_count += 1
    print(f"残り地雷(推定): {mines - flag_count}")

def main():
    rows, cols, mines = 9, 9, 10
    board = create_board(rows, cols)
    place_mines(board, rows, cols, mines)

    while True:
        display_board(board, rows, cols)
        display_remaining_mines(board, mines)
        # ...

def main():
    difficulty = input("難易度を選んでください (E/M/H): ").strip().upper()
    if difficulty == 'E':
        rows, cols, mines = 9, 9, 10
    elif difficulty == 'M':
        rows, cols, mines = 16, 16, 40
    elif difficulty == 'H':
        rows, cols, mines = 16, 30, 99
    else:
        rows, cols, mines = 9, 9, 10  # デフォルト

    board = create_board(rows, cols)
    place_mines(board, rows, cols, mines)
    # あとは同じ
        
if __name__ == "__main__":
    main()

