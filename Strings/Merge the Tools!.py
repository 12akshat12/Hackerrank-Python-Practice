def merge_the_tools(string, k):
    # your code goes here
    for x in range(0,len(string),k):
        p = []
        for j in (string[x:x+k]):
            if j not in p:
                p.append(j)
            else:
                pass
        print("".join(p))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)