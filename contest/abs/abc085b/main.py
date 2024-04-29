def solve(N, allArr):
  riceCakeSet = set(allArr)
  return len(riceCakeSet)

N = int(input())
allArr = [int(input()) for _ in range(N)]

print(solve(N, allArr))