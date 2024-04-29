def can_form_string(S):
    while len(S) > 0:
        if S.endswith('dream'):
            S = S[:-5]  # remove 'dream'
        elif S.endswith('dreamer'):
            S = S[:-7]  # remove 'dreamer'
        elif S.endswith('erase'):
            S = S[:-5]  # remove 'erase'
        elif S.endswith('eraser'):
            S = S[:-6]  # remove 'eraser'
        else:
            return "NO"
    return "YES"

# 入力を受け取る
S = input().strip()

# 結果を出力する
print(can_form_string(S))
