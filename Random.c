from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    """随机生成一个漫步数据"""

    def __init__(self,num_points=5000):
        """初始化随机漫步属性"""
        self.num_points = num_points

        #所有随机漫步都始于（0.0）
        self.x_values = [0]
        self.y_values = [0]

    def file_walk(self):
        """计算随机漫步所有的点"""
        while len(self.x_values) < self.num_points:
            x_direction = choice([1,-1])
            x_distance  = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue
            #计算下一个点的x,y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

rw = RandomWalk()
rw.file_walk()

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,s=15)
#隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()
