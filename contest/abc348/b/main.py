import numpy as np

def solve(N, XYList):
  for i in range(N):
    dList = []
    for j in  range(N):
      dList.append(np.linalg.norm(XYList[i]) - (XYList[j]))

    print(dList)

  return 

def main():

  N = int(input())
  XYList = []
  for _ in range(N):
    XYList.append(list(map(int, input().split())))

  print(solve(N, XYList))

if __name__ == '__main__':
  main()