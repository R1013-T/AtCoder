def solve(S, T):
    n = len(S)
    t1, t2, t3 = T[0], T[1], T[2]

    # 3文字の部分列が一致するか確認
    for i in range(n):
        if S[i].upper() == t1:
            for j in range(i + 1, n):
                if S[j].upper() == t2:
                    for k in range(j + 1, n):
                        if S[k].upper() == t3:
                            return 'Yes'

    # 2文字の部分列に'X'を加えて一致するか確認
    if t3 == 'X':
        for i in range(n):
            if S[i].upper() == t1:
                for j in range(i + 1, n):
                    if S[j].upper() == t2:
                        return 'Yes'

    return 'No'


S = input()
T = input()

print(solve(S, T))
