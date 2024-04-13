def solve(N, arrA):
  return -sum(arrA)


N = int(input())
arrA  = list(map(int, input().split()))

print(solve(N, arrA))
