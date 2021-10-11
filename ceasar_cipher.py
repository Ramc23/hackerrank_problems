#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    arr = list(s)
    cipherarr= list()
    for c in arr:
        
        if c.isupper():
            val = (ord(c) + k - 65)%26 + 65
        elif c.islower():
            val = (ord(c) + k - 97)%26 + 97
        else:
            val = ord(c)
        
        val = chr(val)
        cipherarr.append(val)
       
    return ''.join(cipherarr)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
