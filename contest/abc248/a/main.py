def solve():
    S = input()
    for i in range(10):
      if str(i) not in S:
        return i


print(solve())
