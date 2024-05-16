def solve(correct_character, invalid_character):
    result = []
    s_index = 0
    for t_index in range(len(invalid_character)):
        if s_index < len(correct_character) and correct_character[s_index] == invalid_character[t_index]:
            result.append(str(t_index + 1))
            s_index += 1

    return ' '.join(result)


def main():

    S = input()
    T = input()

    print(solve(S, T))


if __name__ == '__main__':
    main()
