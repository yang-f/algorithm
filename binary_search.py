# -*- coding: utf-8 -*-
'''
Θ(lgn)
'''
def binary_search(a,start,end,key):
    if start==end:
        return -1
    midle = start + int((end - start)/2);
    if a[midle] == key:
        return midle
    elif a[midle] > key:
            return binary_search(a,start,midle,key)
    else:
        return binary_search(a,midle+1,end,key)

a = [1,3,4,5,6,77]
print binary_search(a,0,len(a)-1,6)