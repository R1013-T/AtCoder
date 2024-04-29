def solve(N, AList):
    list = []
    for A in AList:
        list.append(A)
        while len(list) > 1 and list[-1] == list[-2]:
            s = list.pop() + 1
            list.pop()
            list.append(s)

    return len(list)


def main():

    N = int(input())
    AList = list(map(int, input().split()))

    print(solve(N, AList))


if __name__ == "__main__":
    main()
