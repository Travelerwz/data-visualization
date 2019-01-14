#颜色映射

import matplotlib.pyplot as plt

#x_value = [1,2,3,4,5,6]
#y_value = [1,4,9,16,25]
x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]
#绘制散点图
plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Blues,s=40)
#设置图表
plt.title("test")
plt.xlabel("value",fontsize = 14)
plt.ylabel("Numbers",fontsize=24)

#设置每个班坐标轴的取值范围
plt.axis([1,1100,0,1100000])
#设置刻度大小
plt.tick_params(axis='both',which='major',labelsize=14)

#保存图片
plt.savefig('testplot.png',bbox_inches='tight')
plt.show()





