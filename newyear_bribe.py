#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import cycle

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribes = 0
    for I in range(1, n + 1): # for each person I in the list
        index = q.index(I)
        if I - index > 3: # more than two bribes
            print("Too chaotic")
            return
        for j in range(index): # for each number to the left of I, if greater than I,               count it as a bribe
            if q[j] > I: 
                bribes = bribes + 1
    print(str(bribes))

            

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
