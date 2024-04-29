def solve(N ,AArr):
  Alice = []
  Bob = []
  for i in range(len(AArr)):
    maxA = max(AArr)
    if (i % 2 == 0):
      Bob.append(maxA)
    else:
      Alice.append(maxA)
    AArr.remove(maxA)

    ans = sum(Bob) - sum(Alice)

  return ans

N = int(input())
AArr = list(map(int, input().split()))

print(solve(N, AArr))