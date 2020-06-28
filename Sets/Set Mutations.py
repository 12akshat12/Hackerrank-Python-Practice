def main():
    A = int(input())
    a = set(list(map(int, input().split())))
    N = int(input())
    for i in range(N):
        n1 = input().split()
        op = n1[0]
        r = int(n1[1])
        b = set(list(map(int, input().split())))

        if (op == 'update'):
            a = a | b
        elif (op == 'intersection_update'):
            a = a & b
        elif (op == 'difference_update'):
            a = a - b
        elif (op == 'symmetric_difference_update'):
            a = a ^ b
    print(sum(a))


main()