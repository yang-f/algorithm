# -*- coding: utf-8 -*-
'''
Θ(n+k)
'''
import random

k,n = 100,100

def counting_sort(a):
	s = [0 for i in xrange(k)]
	result = [0 for i in xrange(n)]
	for i in a:
		s[i] += 1
	for i in range(1,k):
		s[i] += s[i-1]

	for i in a[::-1]:
		result[s[i]-1] = i
		s[i] -= 1
	return result
	
x = [random.randint(0,k-1) for i in xrange(n)]
	
print counting_sort(x)