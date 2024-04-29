def solve(N, T, X, Y):
    pt, px, py = 0, 0, 0
    for i in range(N):
        d = abs(px - X[i]) + abs(py - Y[i])
        dt = T[i] - pt
        if dt < d:
            return "No"
        if (dt - d) % 2 == 1:
            return "No"

        pt = T[i]
        px = X[i]
        py = Y[i]
    
    return "Yes"

def main():
    N = int(input())
    T = []
    X = []
    Y = []
    for _ in range(N):
        t, x, y = map(int, input().split())
        T.append(t)
        X.append(x)
        Y.append(y)
    
    print(solve(N, T, X, Y))

if __name__ == "__main__":
    main()
