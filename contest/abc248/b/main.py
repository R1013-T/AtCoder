def solve():
    A, B, K = map(int, input().split())

    currentA = A
    cnt = 0
    while currentA < B:
        currentA *= K
        cnt += 1
    
    return cnt


print(solve())