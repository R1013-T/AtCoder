def solve(N, Q, T):
  exists = []
  for i in range(len(T)):
    if T[i] in exists:
      exists.remove(T[i])
    else:
      exists.append(T[i])

  return N - len(exists)

N, Q = map(int, input().split())
T = list(map(int, input().split()))

print(solve(N, Q, T))