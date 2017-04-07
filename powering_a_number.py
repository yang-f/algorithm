# -*- coding: utf-8 -*-
'''
Θ(lgn)
'''
import math
def powering_a_number(x,n):
	if n == 1:
		return x
	if n == 0:
		return 1
	y = powering_a_number(x,math.floor(n/2))
	return y * y * powering_a_number(x,n-2*math.floor(n/2))

print powering_a_number(2,10)