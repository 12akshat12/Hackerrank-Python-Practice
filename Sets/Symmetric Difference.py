def main():
    M=int(input())
    m=map(int, input().split())
    N=int(input())
    n=map(int, input().split())
    a=set(list(m))
    b=set(list(n))
    c=a.symmetric_difference(b)
    for i in sorted(c):
        print(i)


main()