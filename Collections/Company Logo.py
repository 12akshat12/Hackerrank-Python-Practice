import math
import os
import random
import re
import sys
from collections import Counter


def main(string):
    r = sorted(string)
    for i in Counter(r).most_common(3):
        print(*i)


if __name__ == '__main__':
    s = input()
    string = main(s)