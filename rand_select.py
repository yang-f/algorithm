# -*- coding: utf-8 -*-
'''
Θ(n)
'''
import random

def rand_select(a, start, end, k):
	if start == end:
		return a[start]

	tmp 	= random.randint(start, end-1)
	flag 	= a[tmp]
	mid 	= start

	for i in range(start, end):
		if a[i] > flag:
			a[mid],a[i] = a[i],a[mid]
			if mid == tmp:
				tmp = i
			mid 	+= 1
	a[mid],a[tmp] = a[tmp],a[mid]
	if mid < k-1:
		return rand_select(a,mid+1,end,k)
	return rand_select(a,start,mid,k)


x = [random.randint(0,100) for i in xrange(100)]

print rand_select(x, 0, 100, 10)