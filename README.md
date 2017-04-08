笔记
---------------------
* 运行时间:
	* 输入（举个例子：如果是有序的，时间会相应减少。最坏情况是相反排序。）
	* 输入规模
	* 运行时间上界（对用户的承诺。）
* 分析方式:
	* 最坏
		* T(n) = 最长时间 
		* 计算机
		* 相对速度
	* 平均
		* T(n) = 期望时间（加权平均）
	* 最好
		* T(n) = 最短时间（假象）
* 算法大局观:
	* 渐进分析
	* 忽略依赖机器的常量
	* 不是实际的运行时间

* 解递归式的3种方法： 
	* 代换法 猜答案、解出常数、用数学归纳法 
	* 递归树法 把式子分解开，画成树的形状，持续展开，逐层求和 
	* 主定理 T(n)=aT(n/b)+f(n),a>=1,b>1,f(n)渐进趋正 和n^logba比较

* 分治法：
	* 分divide
	* 治conquer
	* 合combine

* 斐波那契数列:
	* 这个数列从第三项开始，每一项都等于前两项之和
	* Θ(lgn)
	```
	⎡f(n+1) f(n)⎤ = ⎡1 1⎤^n
	⎣f(n) f(n-1)⎦   ⎣1 0⎦
	```

* 斯特拉森矩阵乘法:
	* Θ(n^lg7)
	```
	    a11 a12     b11 b12	 
	A = a21 a22 B = b21 b22
	```
	```
	x1 = (a11 + a22) * (b11 + b22);
	x2 = (a21 + a22) * b11;
	x3 = a11 * (b12 - b22);
	x4 = a22 * (b21 - b11);
	x5 = (a11 + a12) * b22;
	x6 = (a21 - a11) * (b11 + b12);
	x7 = (a12 - a22) * (b21 + b22);
	```
	```
	c11 = x1 + x4 - x5 + x7
	c12 = x3 + x5
	c21 = x2 + x4
	c22 = x1 + x3 - x2 + x6
	```
	```
	    c11 c12
	C = c21 c22
	```
