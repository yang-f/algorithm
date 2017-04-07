# -*- coding: utf-8 -*-
'''
	⎡f(n+1) f(n)⎤ = ⎡1 1⎤^n
	⎣f(n) f(n-1)⎦	⎣1 0⎦
'''
import numpy
import math

start = [[1,1],[1,0]]

def fibonacci_sequence(n):
   if n <= 1:
       return n
   else:
       return(fibonacci_sequence(n-1) + fibonacci_sequence(n-2))


def fibonacci_sequence_divide(n):
	if n == 1:
		return start
	if n == 0:
		return 1
	y = fibonacci_sequence_divide(math.floor(n/2))
	z = numpy.dot(y,y)
	return numpy.dot(z,fibonacci_sequence_divide(n-2*math.floor(n/2)))

print fibonacci_sequence_divide(10)[0][1]
print fibonacci_sequence(10)
