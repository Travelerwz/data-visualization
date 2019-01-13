#绘制散点图

import matplotlib.pyplot as plt

#x_value = [1,2,3,4,5,6]
#y_value = [1,4,9,16,25]
x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]
#绘制散点图
plt.scatter(x_value,y_value,s=100)
#设置图表
plt.title("test")
plt.xlabel("value",fontsize = 14)
plt.ylabel("Numbers",fontsize=24)

#设置每个班坐标轴的取值范围
plt.axis([1,1100,0,1100000])
#设置刻度大小
plt.tick_params(axis='both',which='major',labelsize=14)

#删除点的轮廓,修改颜色
plt.scatter(x_value,y_value,c='red',edgecolors='none',s=30)
plt.show()




