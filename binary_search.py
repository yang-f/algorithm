# -*- coding: utf-8 -*-
'''
Θ(lgn)
'''
def binary_search(a,key):
	if a[int(len(a)/2)] == key:
		return int(len(a)/2)
	elif a[int(len(a)/2)] > key:
		return binary_search(a[:int(len(a)/2)],key)
	else:
		return binary_search(a[int(len(a)/2):],key)

print binary_search([1,3,4,5,6,77],3)