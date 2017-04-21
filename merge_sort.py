# -*- coding: utf-8 -*-
'''
Θ(nlgn)
'''
import math
import random

def merge_sort(a):
	if len(a) == 1:
		return a

	left = merge_sort(a[:int(math.ceil(len(a)/2))])
	right = merge_sort(a[int(math.ceil(len(a)/2)):])

	i,j = 0,0
	result = []
	while i < len(left) and j < len(right):
		if left[i] >= right[j]:
			result.append(right[j])
			j += 1
		else:
			result.append(left[i])
			i += 1	

	result += left[i:]
	result += right[j:] 
	
	return result

x = [random.randint(0,100) for i in xrange(100)]

print merge_sort(x)