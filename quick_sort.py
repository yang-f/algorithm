# -*- coding: utf-8 -*-
'''
Θ(n^2)
'''
import random

def quick_sort(a,start,end):
	if start < end:
		flag 	= a[start]
		mid 	= start
		for i in range(start+1, end):
			if a[i] < flag:
				a[mid],a[i] = a[i],a[mid]
				mid 	+= 1
		a[mid] = flag
		quick_sort(a, start, mid)
		quick_sort(a, mid+1, end)
	return a


x = []
for k in range(100):
	x.append(random.randint(0, 100))
print quick_sort(x, 0, 100)