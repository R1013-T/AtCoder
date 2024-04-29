def solve(N, Y):
    # 外側のループで10,000円札の枚数を決定
    for tenNum in range(N + 1):
        # 内側のループで5,000円札の枚数を決定
        for fiveNum in range(N + 1 - tenNum):
            # 1,000円札の枚数を計算
            oneNum = N - tenNum - fiveNum
            # 総金額がY円になるかチェック
            if 10000 * tenNum + 5000 * fiveNum + 1000 * oneNum == Y:
                return f"{tenNum} {fiveNum} {oneNum}"
    
    return "-1 -1 -1"

N, Y = map(int, input().split())
print(solve(N, Y))
