from collections import OrderedDict

n=int(input())
d=OrderedDict()
for i in range (n):
    m=input()
    if(m in d):
        d[m]=d[m]+1
    else:
        d[m] = 1
print(len(d))
for i in d.values():
    print(i, end=' ')
