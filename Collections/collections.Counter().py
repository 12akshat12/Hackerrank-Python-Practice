from collections import Counter

def main():
    sm = 0
    X = int(input())
    n = list(map(int, input().split()))
    c = Counter(n)
    N = int(input())
    for i in range (N):
        s, x = map(int, input().split())
        if(c[s] > 0):
            sm = sm + x
            c[s] = c[s] - 1
    print(sm)


main()