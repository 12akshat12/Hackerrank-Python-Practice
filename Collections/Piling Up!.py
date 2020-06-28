T=int(input())
for i in range (T):
    N=int(input())
    n=list(map(int, input().split()))
    i=0
    l=len(n)
    while(i<l-1 and n[i]>=n[i+1]):
        i=i+1
    while(i<l-1 and n[i]<=n[i+1]):
        i=i+1
    if(i==l-1):
        print('Yes')
    else:
        print('No')
