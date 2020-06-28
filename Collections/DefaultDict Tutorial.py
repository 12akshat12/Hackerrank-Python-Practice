from collections import defaultdict

def main():
    n, m = map(int, input().split())
    d1=defaultdict(list)
    l=[]
    for i in range (n):
        x=input()
        d1[x].append(i+1)
    for j in range (m):
        y=input()
        l.append(y)
    for i in l:
        if(i in d1):
            print(*d1[i])
        else:
            print(-1)


main()
