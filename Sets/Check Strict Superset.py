def main():
    flag=0
    A=set(map(int, input().split()))
    N=int(input())
    for i in range (N):
        n=set(map(int, input().split()))
        if(len(A)>len(n)):
            if(A.issuperset(n)):
                flag=1
            else:
                flag=0
                break
        else:
            flag=0
            break
    if(flag==0):
        print('False')
    else:
        print('True')
main()