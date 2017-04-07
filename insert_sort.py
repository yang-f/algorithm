# -*- coding: utf-8 -*-
'''
Θ(n^2)
'''
import random

def insert_sort(a):
	for i in range(1,len(a)):
		temp = a[i]
		j = i - 1
		while j > -1 and temp < a[j]:
			a[j+1] = a[j]
			j -= 1
		a[j+1] = temp

	return a

x = []
for k in range(100):
	x.append(random.randint(0,100))
print insert_sort(x)