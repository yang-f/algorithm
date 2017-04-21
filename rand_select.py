# -*- coding: utf-8 -*-
'''
'''
import random

def rand_select(a, start, end, k):
	if start == end:
		return a[start]

	flag 	= a[random.randint(start, end-1)]
	mid 	= start

	for i in range(start, end):
		if a[i] < flag:
			a[mid],a[i] = a[i],a[mid]
			mid 	+= 1

	if mid < k:
		return rand_select(a,mid+1,end,k)
	return rand_select(a,start,mid,k)


x = [random.randint(0,100) for i in xrange(100)]

print rand_select(x, 0, 100, 50)