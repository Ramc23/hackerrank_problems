#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    plus = 0
    minus = 0 
    zero = 0
    n = len(arr)
    
    for x in arr:
        if (x > 0):
            plus = plus+1
        elif (x < 0):
            minus = minus +1
        else:
            zero =zero+1
            
    pluspercent = plus/n
    minuspercent = minus/n
    zeropercent = zero/n
    print("{:.6f}".format(pluspercent))
    print("{:.6f}".format(minuspercent))
    print("{:.6f}".format(zeropercent))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
