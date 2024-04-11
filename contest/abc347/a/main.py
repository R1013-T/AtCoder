def solve(N, K, A):
    KMultipleArr = []
    for i in A:
        if i % K == 0:
          KMultipleArr.append(i)

    for i in range(len(KMultipleArr)):
      KMultipleArr[i] = KMultipleArr[i] // K
    
    return ' '.join(map(str, KMultipleArr))


N, K = map(int, input().split())
A = list(map(int, input().split()))

print(solve(N, K, A))