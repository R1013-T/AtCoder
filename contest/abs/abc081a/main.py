def solve(arr):
  cnt = 0
  str_arr = str(arr)
  for i in str_arr:
      if i == '1':
        cnt += 1
  return cnt

arr = list(map(int, input().split()))

print(solve(arr))