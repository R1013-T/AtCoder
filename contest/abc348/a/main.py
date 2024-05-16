def solve(N):
  ans = ''
  for i in range(1, N + 1):
    if i % 3 == 0:
      ans += 'x'
    else:
      ans += 'o'

  return ans

def main():

  N = int(input())

  print(solve(N))

if __name__ == "__main__":
  main()