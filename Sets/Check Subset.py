def main():
    T=int(input())
    for i in range (T):
        N=int(input())
        n=set(map(int, input().split()))
        M=int(input())
        m=set(map(int, input().split()))
        print(n.issubset(m))
main()