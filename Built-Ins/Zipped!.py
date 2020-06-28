N, X = map(int, input().split())
n = []
for i in range(X):
    n.append(list(map(float, input().split())))
for i in range(N):
    s = 0
    for j in range(X):
        s += n[j][i]
    avg = s / X
    print(avg)

