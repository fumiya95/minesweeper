## ステップ1：プロジェクトの初期セットアップ

#1. ディレクトリを作成（例: `minesweeper/`）。
#2. `minesweeper.py`（メインファイル）と `.gitignore` を用意する。
#3. 最低限のコードを置いてみる。

#python
# minesweeper.py

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