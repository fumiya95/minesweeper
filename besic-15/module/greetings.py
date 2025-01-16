def say (name):
    print(f"{name}です。")

var = "greetings.pyの変数です"

print("greetings.pyの__name__:",__name__)

if __name__ == "__main__":
    print("__name__が実行")
    say("テスト")