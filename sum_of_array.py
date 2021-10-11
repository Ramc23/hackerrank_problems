#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    res =0
    for x in ar:
        res = res + x
    return res


if __name__ == '__main__':
   # fptr = open(os.environ['Documents//result.txt'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print(str(result))

    #fptr.write(str(result) + '\n')

   # fptr.close()
