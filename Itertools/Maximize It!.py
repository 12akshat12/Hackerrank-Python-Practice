from itertools import product

def main():
    KM = list(map(int, input().split()))
    K = KM[0]
    M = KM[1]
    s, mx = 0, 0
    arr, brr = [], []
    for i in range (K):
        X = list(map(int, input().split()))
        arr.append(X[1:])
    N=product(*arr)
    for i in N:
        for j in i:
            s=s+(j**2)
        brr.append(s%M)
        s=0
    print(max(brr))


main()