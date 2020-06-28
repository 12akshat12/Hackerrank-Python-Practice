from itertools import groupby

S = input()
arr=[]
for seq, cnt in groupby(S):
    arr.append((len(list(cnt)), int(seq)))
print(*arr)