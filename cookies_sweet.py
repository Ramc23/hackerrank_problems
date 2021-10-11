#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    
    ll = sorted(A)
    count =0
    print(ll)
    while True:
        first = ll.pop(0)
        
        if first > k:
            print(ll)
            return count
        
        if len(ll) == 0:
            return -1
        
        second = ll.pop(0)
        new = first + (2* second)
        ll.append(new)
        ll = sorted(ll)
        count +=1
        
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
