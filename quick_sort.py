# -*- coding: utf-8 -*-
'''
Θ(nlgn)
'''
import random

def quick_sort(a, start, end):
	if start < end:
		tmp 	= random.randint(start, end-1)
		flag 	= a[tmp]
		mid 	= start
		for i in range(start, end):
			if a[i] < flag:
				a[mid],a[i] = a[i],a[mid]
				if mid == tmp:
					tmp = i
				mid 	+= 1
		a[mid],a[tmp] = a[tmp],a[mid]

		quick_sort(a, start, mid)
		quick_sort(a, mid+1, end)
	return a


x = [random.randint(0,10) for i in xrange(10)]
print x
print quick_sort(x, 0, 10)