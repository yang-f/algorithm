# -*- coding: utf-8 -*-
'''
运行时间:
	输入（举个例子：如果是有序的，时间会相应减少。最坏情况是相反排序。）
	输入规模
	运行时间上界（对用户的承诺。）
分析方式：
	最坏
		T(n) = 最长时间 
		计算机
		相对速度
	平均
		T(n) = 期望时间（加权平均）
	最好
		T(n) = 最短时间（假象）
算法大局观
	渐进分析
	忽略依赖机器的常量
	不是实际的运行时间
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