import math

def main():
    N=int(input())
    M=int(input())
    print(round(math.degrees(math.atan(N/M))),end="°")
main()