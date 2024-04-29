def solve(N, AArr, BArr):
    for i in range(N):
        A = AArr[i]
        B = BArr[i]
        if A != B:
            for j in range(max(len(A), len(B))):
                if (A[j] != B[j]):
                    return (f'{i + 1} {j + 1}')
    return


def main():

    N = int(input())
    AArr = []
    BArr = []

    for _ in range(N):
        AArr.append(input())
    for _ in range(N):
        BArr.append(input())

    print(solve(N, AArr, BArr))


if __name__ == "__main__":
    main()
