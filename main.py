from db import create_table, add_memo, get_memos, delete_memo


def show_menu():
    print("\n=== メモアプリ ===")
    print("1. メモ追加")
    print("2. メモ一覧表示")
    print("3. メモ削除")
    print("4. 終了")


def main():
    create_table()

    while True:
        show_menu()
        choice = input("番号を選んでください: ")

        if choice == "1":
            content = input("メモ内容を入力してください: ").strip()
            if content == "":
                print("空のメモは追加できません。")
            else:
                add_memo(content)
                print("メモを追加しました。")

        elif choice == "2":
            memos = get_memos()
            if len(memos) == 0:
                print("メモはまだありません。")
            else:
                print("\n--- メモ一覧 ---")
                for memo in memos:
                    print(f"ID: {memo[0]} | 内容: {memo[1]} | 作成日時: {memo[2]}")

        elif choice == "3":
            memo_id = input("削除したいメモのIDを入力してください: ")
            if memo_id.isdigit():
                delete_memo(int(memo_id))
                print("メモを削除しました。")
            else:
                print("数字のIDを入力してください。")

        elif choice == "4":
            print("アプリを終了します。")
            break

        else:
            print("1〜4の番号を入力してください。")


if __name__ == "__main__":
    main()