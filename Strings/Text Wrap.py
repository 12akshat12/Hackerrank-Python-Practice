import textwrap

def wrap(string, max_width):
    wr=textwrap.wrap(string,width=max_width)
    return ('\n'.join(wr))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)