from collections import deque


def main():
    N = int(input())
    d = deque()
    for i in range(N):
        n = input().split()
        if (n[0] == 'append'):
            d.append(n[-1])
        elif (n[0] == 'pop'):
            d.pop()
        elif (n[0] == 'popleft'):
            d.popleft()
        else:
            d.appendleft(n[-1])
    print(*d)


main()