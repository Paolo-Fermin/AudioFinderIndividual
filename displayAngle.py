from graphics import *
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

file1 = os.path.join(os.getcwd(), 'signal1.txt')
file2 = os.path.join(os.getcwd(), 'signal2.txt')

with open(file1, 'r') as left_signal:
    csv_reader = csv.reader(left_signal, delimiter = '\n')
    #for row in csv_reader:
        #print(row)

table = pd.read_table(file1, header=None, names=['Left'])
table2 = pd.read_table(file2, header=None)
table.insert(1, 'Right', table2, True)

table['Difference'] = table['Left'] - table['Right']

print(table['Difference'])
avg_diff = table['Difference'].mean()

print(table)
print(avg_diff)

left_max_index = table['Left'].idxmax()
right_max_index = table['Right'].idxmax()

print(left_max_index)
print(right_max_index)

c = 343
l = .1
T = 1e-3

left_time = left_max_index * (T/len(table.index))
right_time = right_max_index * (T/len(table.index))

print("left time = " + str(left_time))
print("right time = " + str(right_time))

left_dist = left_time * c
right_dist = right_time * c

print("left dist = " + str(left_dist))
print("right dist = " + str(right_dist))

if (left_time >= right_time) :
    angle = np.arccos(right_dist/l)
    angle_degrees = np.degrees(angle)
else:
    angle = np.arccos(left_dist/l)
    angle_degrees = np.degrees(angle)

print("angle = " + str(angle))
print("angle (degrees) = " + str(angle_degrees))


win = GraphWin('Speaker Angle', 1000, 750)
origin = Point(win.getWidth()/2, win.getHeight() - 10)
origin.draw(win)

radius = win.getWidth()/2 - 50

cir = Circle(origin, radius)
cir.setWidth(5)
cir.draw(win)

endpoint = Point( origin.getX() + cir.getRadius() * np.cos(angle), origin.getX() - cir.getRadius() * np.sin(angle))

angle_line = Line(origin, endpoint)
angle_line.setFill('red')
angle_line.setWidth(5)
angle_line.draw(win)

title = Text(Point(win.getWidth()/2 - 30, 30), '1KHz Audio Direction')
title.draw(win)

angle_label = Text(Point(win.getWidth() / 2 - 30, 50), "{:.2f} degrees".format(angle_degrees))
angle_label.draw(win)

#pause to view results
win.getMouse()
win.close()

'''
plt.figure()
plt.plot(table['Left'])
plt.plot(table['Right'])
plt.plot(table['Difference'])
plt.show()
'''