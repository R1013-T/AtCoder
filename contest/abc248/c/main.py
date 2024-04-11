def solve(N, M, K):
    mod = 998244353
    # dpテーブルの初期化
    dp = [[0] * (K+1) for _ in range(N+1)]
    dp[0][0] = 1  # 0個選んだときの和が0である場合の数は1

    # DPテーブルを更新していく
    for i in range(1, N+1):
        for j in range(K+1):
            for a in range(1, M+1):
                if j-a >= 0:
                    dp[i][j] += dp[i-1][j-a]
                    dp[i][j] %= mod

    # 答えの計算
    ans = 0
    for j in range(K+1):
        ans += dp[N][j]
        ans %= mod

    return ans

# 入力
N, M, K = map(int, input().split())
# 解の計算と出力
print(solve(N, M, K))