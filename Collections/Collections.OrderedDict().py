from collections import OrderedDict

def main():
    d=OrderedDict()
    N=int(input())
    for i in range (N):
        item_name, space, net_price=input().rpartition(' ')
        if(item_name not in d):
            d[item_name]=int(net_price)
        else:
            d[item_name]=d[item_name]+int(net_price)
    for i in d.items():
        print(i[0], i[1])


main()
