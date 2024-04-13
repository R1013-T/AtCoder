def solve(n, arr):
  cnt = 0
  while all( a % 2 == 0 for a in arr):
    arr = [a // 2 for a in arr]
    cnt += 1
  return cnt


n = int(input())
arr = list(map(int, input().split()))

print(solve(n, arr))