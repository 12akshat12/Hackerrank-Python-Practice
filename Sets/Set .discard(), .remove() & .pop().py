n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range (N):
    t=list(input().split())
    if(t[0]=='pop'):
        s.pop()
    elif(t[0]=='remove'):
        s.remove(int(t[1]))
    else:
        s.discard(int(t[1]))
print(sum(s))