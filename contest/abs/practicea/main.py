def solve(a, b, c, s):
    sum = a + b + c
    ans = str(sum) + ' ' + s
    return ans


a = int(input())
b, c = map(int, input().split())
s = input()

print(solve(a, b, c, s))