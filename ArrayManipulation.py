# method 1 
# times runout for longer cases

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    res = [0]*n
    maxele = 0
    for q in range(len(queries)-1):
        for i in range(queries[q][0]-1, queries[q][1]):
            res[i] += queries[q][2]
    maxele1 = max(res)
    for j in range((queries[-1][0])-1, queries[-1][1]):
        maxele = max(res[j],maxele)
    maxele += queries[-1][2]
    return(max(maxele,maxele1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()


# method 2
# DIFFERENCE ARRAY

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    list = [0]*(n+1)
    for q in queries:
        x, y, incr = q[0],q[1],q[2]
        list[x-1] += incr
        if((y)<=len(list)): list[y] -= incr;
    max = x = 0
    for i in list:
        x=x+i;
        if(max<x): max=x;
    return(max)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
