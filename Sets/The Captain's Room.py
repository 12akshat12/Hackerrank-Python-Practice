def main():
    k=int(input())
    n=list(map(int, input().split()))
    s1=set()
    s2=set()
    for i in n:
        if(i not in s1):
            s1.add(i)
        else:
            s2.add(i)
    print((s1.difference(s2)).pop())
main()