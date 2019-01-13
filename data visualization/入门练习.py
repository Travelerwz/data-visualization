#绘制折线图

import matplotlib.pyplot as plt

squares = [1,4,9,16,25]

#线条的粗细
plt.plot(squares,linewidth=5)

#图表标题，x/y轴的标签
plt.title("test")
plt.xlabel("value",fontsize = 24)
plt.ylabel("Square of Value",fontsize = 24)

#刻度标记的大小
plt.tick_params(axis='both',labelsize=14)
plt.plot(squares)
plt.show()