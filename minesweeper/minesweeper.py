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