import builtins
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(builtins.hash(integer_list))
