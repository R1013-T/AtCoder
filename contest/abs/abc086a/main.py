def solve(a, b):
  ans = (a * b) % 2
  if (ans == 0):
    return 'Even'
  else:
    return 'Odd'


a, b = map(int, input().split())

print(solve(a, b))