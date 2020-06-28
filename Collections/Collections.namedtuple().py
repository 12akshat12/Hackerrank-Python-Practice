from collections import namedtuple
N=int(input())
col=input().split()
s=0
data=namedtuple('data',col)
for i in range (N):
    d=data(*input().split())
    s=s+int(d.MARKS)
print(s/N)
