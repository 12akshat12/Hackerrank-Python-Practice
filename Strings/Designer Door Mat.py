## In O(n) with some basic pattern logic

def main():
    a = 1
    b = '.|.'
    d = '-'
    NM = input().split()
    N = int(NM[0])
    M = int(NM[1])
    c = int(M - len(b)) // 2
    for i in range(N):
        if (i < ((N / 2) - 1)):
            print(c * d + b + c * d)
            a = a + 2
            b = '.|.' * a
            c = (M - len(b)) // 2

        elif (i == (int(N / 2))):
            e = (M - 7) // 2
            print(e * d + "WELCOME" + e * d)

        elif (i > ((N / 2))):
            a = a - 2
            b = '.|.' * a
            c = (M - len(b)) // 2
            print(c * d + b + c * d)


main()