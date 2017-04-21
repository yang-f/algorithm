# -*- coding: utf-8 -*-
'''
Θ(n)
'''
import random
import math
def partition(a,p,r,x):
    low = [m for m in a if m < x]
    high = [m for m in a if m > x]
    a[p-1:r] = low + [x] + high 
    return len(low)

def median(a):
    a.sort()
    return a[(len(a)+1)/2 - 1]

def select(a,i):
    if len(a) == 1:
        return a[0]
    groups = []
    numOfGroups = int(math.ceil(len(a)*1.0/5))
    start,end = 0,0
    for j in range(0,numOfGroups-1):
        start = j*5
        end = start + 5
        groups.append(a[start:end]) 
    groups.append(a[end:])

    medians = []
    for g in groups:
        medians.append(median(g))

    x = select(medians,(len(medians)+1)/2)

    k = partition(a,1,len(a),x) + 1

    if k == i :
        return x 
    elif k > i :
        return select(a[0:k],i) 
    else:
        return select(a[k:],i-k)

x = [random.randint(0,100) for i in xrange(100)]

print select(x, 50)