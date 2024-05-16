def solve(groupCount, seatCount, groupList):
    runCount = 1
    currentPassengers = 0
    for i in range(len(groupList)):
        if currentPassengers + groupList[i] <= seatCount:
            currentPassengers += groupList[i]
        else:
            currentPassengers = groupList[i]
            runCount += 1
    return runCount


def main():
    N, K = map(int, input().split())
    AList = list(map(int, input().split()))
    print(solve(N, K, AList))


if __name__ == '__main__':
    main()
