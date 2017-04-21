#!/usr/bin/env python
#encoding=utf-8
 
import math
import random
 
def sort(a, radix=10):
    K = int(math.log(max(a), radix) + 1) if math.log(max(a), radix)%1 == 0  else int(math.ceil(math.log(max(a), radix))) 
    bucket = [[] for i in range(radix)] 
    for i in range(1, K+1): 
        for val in a:
            bucket[val%(radix**i)/(radix**(i-1))].append(val)
        del a[:]
        for each in bucket:
            a.extend(each)
        bucket = [[] for i in range(radix)]
    return a

x = [random.randint(0,100) for i in xrange(100)]

print sort(x)

