def solve(N, A, B):
  trueArray = []
  for i in range(1, N + 1):
    number_str = str(i)
    digits = list(number_str)
    digits_int = [int(d) for d in digits]
    total = sum(digits_int)
    if total >= A and total <= B:
      trueArray.append(i)
  return sum(trueArray)

N, A, B = map(int, input().split())

print(solve(N, A, B))