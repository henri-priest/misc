# Problem: https://www.hackerrank.com/challenges/ctci-making-anagrams/

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):

    # Custom code
    
    union = set(a) & set(b)
    
    count = 0

    for i in a:
        if i not in union:
            count +=1

    for i in b:
        if i not in union:
            count +=1

    for i in union:
        n1 = a.count(i)
        n2 = b.count(i)
        count += abs(n1-n2)
        
    return count

    # / Custom code

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
