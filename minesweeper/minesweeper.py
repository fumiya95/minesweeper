## ステップ1：プロジェクトの初期セットアップ

#1. ディレクトリを作成（例: `minesweeper/`）。
#2. `minesweeper.py`（メインファイル）と `.gitignore` を用意する。
#3. 最低限のコードを置いてみる。

#python
# minesweeper.py
import random

def create_board(rows, cols):
    board = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            cell = {
                'mine': False,
                'revealed': False,
                'flagged': False
            }
            row.append(cell)
        board.append(row)
    return board

def place_mines(board, rows, cols, mines):
    """
    board上に mines 個の地雷をランダムに配置する
    """
    total_cells = rows * cols
    mine_positions = random.sample(range(total_cells), mines)  # インデックスをランダム取得

    for pos in mine_positions:
        r = pos // cols
        c = pos % cols
        board[r][c]['mine'] = True

def main():
    rows, cols, mines = 9, 9, 10
    board = create_board(rows, cols)
    place_mines(board, rows, cols, mines)
    print("地雷を配置しました。")

if __name__ == "__main__":
    main()

def main():
  print("テキストベース マインスイーパーを始めます。")

if __name__ == "__main__":
  main()

# minesweeper.py

def main():
    # ゲームの初期設定
    rows = 9
    cols = 9
    mines = 10
    print(f"{rows} x {cols} の盤面に地雷を {mines} 個配置します。")
    # 実際の処理はまだ書かない
    # ここで設定を変えられるようにするなどの拡張も可能

if __name__ == "__main__":
    main()

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
                'mine': False,   # 地雷があるか
                'revealed': False,  # 開いているか
                'flagged': False    # 旗を立てているか
            }
            row.append(cell)
        board.append(row)
    return board

def main():
    rows, cols, mines = 9, 9, 10
    board = create_board(rows, cols)
    # テスト表示
    print("盤面の初期状態:", board)

if __name__ == "__main__":
    main()