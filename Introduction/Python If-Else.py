import math
import os
import random
import re
import sys

def Solution(n):
    if(n%2!=0):
        return ('Weird')
    else:
        if((n>=2 and n<=5) or (n>20)):
            return ('Not Weird')
        else:
            return ('Weird')

if __name__ == '__main__':
    n = int(input().strip())
    print(Solution(n))