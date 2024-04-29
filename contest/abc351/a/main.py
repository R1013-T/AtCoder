def solve(TScores, AScores):
    TTotal = sum(TScores)
    ATotal = sum(AScores)
    return TTotal - ATotal + 1


AArr = list(map(int, input().split()))
BArr = list(map(int, input().split()))

print(solve(AArr, BArr))
