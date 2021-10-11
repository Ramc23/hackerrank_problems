#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    counter =0
    min =0 
    max =0
    for x in arr:
        if (counter != 4):
            min = min + x
        if (counter != 0):
            max = max + x
        counter = counter +1
    
    print(str(min) + " " +str(max))


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
