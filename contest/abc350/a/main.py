def solve(S):
  name = S[:3]
  number = S[3:]

  ans = 'No'
  if name != 'ABC':
    ans = 'Yes'
    return ans
  
  if int(number) <= 349 and int(number) > 0 and int(number) != 316:
    ans = 'Yes'
    return ans

  return ans

S = input()

print(solve(S))