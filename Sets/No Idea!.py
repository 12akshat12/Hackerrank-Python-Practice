def main():
    h=0
    n, m=map(int, input().split())
    N=list(map(int, input().split()))
    f=set(list(map(int, input().split())))
    s=set(list(map(int, input().split())))
    for i in N:
        if(i in f):
            h=h+1
        elif(i in s):
            h=h-1
    print(h)


main()