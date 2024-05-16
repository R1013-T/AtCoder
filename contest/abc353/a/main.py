def solve(buildingCount, buildingHeightList):
  for i in range(len(buildingHeightList)):
    if buildingHeightList[0] < buildingHeightList[i]:
      return i + 1
  return -1

def main():

  N = int(input())
  HList = list(map(int, input().split()))

  print(solve(N, HList))

if __name__ == '__main__':
  main()