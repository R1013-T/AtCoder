def solve(S):
    cntArr = []
    charArr = []
    for i in range(len(S)):
        isExist = False
        for j in range(len(charArr)):
            if (charArr[j] == S[i]):
                isExist = True
                cntArr[j] += 1

        if (isExist != True):
            charArr.append(S[i])
            cntArr.append(1)

    ans = 'Yes'
    for i in range(len(cntArr)):
      cnt = cntArr.count(cntArr[i])
      if (cnt != 0 and cnt != 2):
          ans = 'No'
          break

    return ans


S = input()

print(solve(S))
