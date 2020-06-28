def main():
    N=int(input())
    n=set(map(int, input().split()))
    M=int(input())
    m=set(map(int, input().split()))
    print(len(n.intersection(m)))
main()