def solve():
    return


def main():

    x = int(input())  # 整数の入力

    s = input()  # 文字列の入力

    # 空白区切りの複数の値の読み込み
    a, b = map(int, input().split())

    # 数列の読み込み
    arr = list(map(int, input().split()))

    print(solve())


if __name__ == "__main__":
    main()
