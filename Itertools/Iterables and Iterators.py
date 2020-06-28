from itertools import combinations

def main():
    N=int(input())
    n=list(input().split())
    K=int(input())
    c=list(combinations(n, K))
    l=len(c)
    s=0
    for i in c:
        if('a' in i):
            s=s+1
    return(s/l)
print(main())
