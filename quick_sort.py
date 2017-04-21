# -*- coding: utf-8 -*-
'''
Θ(nlgn)
'''
import random

def quick_sort(a, start, end):
	if start < end:

		flag 	= a[random.randint(start, end-1)]
		mid 	= start

		for i in range(start, end):
			if a[i] < flag:
				a[mid],a[i] = a[i],a[mid]
				mid 	+= 1

		a[mid] = flag

		quick_sort(a, start, mid)
		quick_sort(a, mid+1, end)
	return a


x = [random.randint(0,100) for i in xrange(100)]
	
print quick_sort(x, 0, 100)