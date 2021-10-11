#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    sum = sumOfDigit(int(n))
    
    if (k >1):
        sum = sum *k
    
    while  sum > 9:
        sum = sumOfDigit(sum) 
    return sum


def sumOfDigit(n):
    tot = 0
    while n >0 :
        dig = n%10
        tot = tot + dig
        n = n//10
    return tot
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
