from scipy.optimize import *
import numpy as np
x_set = [0, 40, 13, 15, 76, 80, 120, 80, 100, 66, 20, 86]
y_set = [0, 6, 33, 119, 145, 132, 139, 112, 80, 73, 60, 40]
w_set = [129, 28, 125, 12, 43, 110, 66, 86, 425, 182, 220, 320]
x1_set = [80, 100, 66, 20, 86]
y1_set = [112, 80, 73, 60, 40]
value_default = 10000
#挑选某一个点作为分配中心，其余点仍作为消耗点
#另外，也可以生成5*12的距离矩阵
#w_set为需求量，简化认为费用=需求量*距离，实际上将单位距离运费均视为1
for j in range(0, len(x1_set), 1):
	for i in range(0, len(x_set), 1):
		delta_x = x1_set[j] - x_set[i]
		delta_y = y1_set[j] - y_set[i]
		delta_x_square = delta_x ** 2
		delta_y_square = delta_y ** 2
		value_default = value_default +w_set[i] * ((delta_x_square + delta_y_square) ** 0.5)
	print([x1_set[j], y1_set[j], value_default])
	value_default = 10000

