def solve(S: str):
    
    subStrings = set()

    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            subString = S[i:j]
            subStrings.add(subString)
    
    return len(subStrings)

S = input()

print(solve(S))