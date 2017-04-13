# -*- coding: utf-8 -*-
'''
	Θ(n^lg7)
'''
import numpy as np
import time

def strassen(a,b):

	if len(a) == 2:
		return np.dot(a,b)

	m = len(a)/2

	a11 = a[:m,:m]
	a12 = a[:m,m:]
	a21 = a[m:,:m]
	a22 = a[m:,m:]

	b11 = b[:m,:m]
	b12 = b[:m,m:]
	b21 = b[m:,:m]
	b22 = b[m:,m:]

	x1 = strassen((a11 + a22), (b11 + b22))
	x2 = strassen((a21 + a22), b11)
	x3 = strassen(a11, (b12 - b22))
	x4 = strassen(a22, (b21 - b11))
	x5 = strassen((a11 + a12), b22)
	x6 = strassen((a21 - a11), (b11 + b12))
	x7 = strassen((a12 - a22), (b21 + b22))

	c11 = x1 + x4 - x5 + x7
	c12 = x3 + x5
	c21 = x2 + x4
	c22 = x1 + x3 - x2 + x6

	c1 = np.hstack((c11,c12)) 
	c2 = np.hstack((c21,c22)) 

	return np.vstack((c1,c2))


x = y = np.arange(64).reshape(8, 8)

t = time.time()
print np.dot(x, y)
print time.time() - t

t = time.time()
print strassen(x, y)
print time.time() - t