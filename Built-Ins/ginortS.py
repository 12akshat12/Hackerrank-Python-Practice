# 1st Method
# s='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
# print(*sorted(input(), key=s.index), sep='')


# 2nd Method
s1=input()
s2=''
s2+=''.join(sorted((c) for c in s1 if c.islower()))
s2+=''.join(sorted((c) for c in s1 if c.isupper()))
s2+=''.join(sorted((c) for c in s1 if c.isdigit() and (int(c)%2!=0)))
s2+=''.join(sorted((c) for c in s1 if c.isdigit() and c not in s2))
print(s2)