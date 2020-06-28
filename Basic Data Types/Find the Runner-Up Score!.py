import copy
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    brr=set(arr)
    brr.remove(max(list(brr)))
    print(max(brr))
