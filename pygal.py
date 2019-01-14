from random import randint
import pygal
class Die():
    def __init__(self,num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1,self.num_sides)

die = Die()
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

#分析结果
frequence = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequence.append(frequency)

hist = pygal.Bar()
hist.title = "result test"
hist.x_labels = ['1','2','3','4','5','6']
hist.add('D6',frequence)
hist.render_to_file('die_visual.svg')
