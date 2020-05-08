from graphics import *
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import pdb


c = 343.0
l = .1
T = 1e-3

left_file = os.path.join(os.getcwd(), 'left_signal.txt')
right_file = os.path.join(os.getcwd(), 'right_signal.txt')


table = pd.read_csv(left_file)
table.rename(columns={'signal':'left'}, inplace=True)
table2 = pd.read_csv(right_file)
#pdb.set_trace()

table = table.join(table2['signal'])
table.rename(columns={'signal':'right'}, inplace=True)

left_min_index = table['left'].idxmin()
right_min_index = table['right'].idxmin()

print(left_min_index)
print(right_min_index)


time_interval = T / len(table.index)
print("time interval = " + str(time_interval))

left_time = table.loc[left_min_index, 'time']
right_time = table.loc[right_min_index, 'time']
deltaT = left_time - right_time

print("left time = " + str(left_time))
print("right time = " + str(right_time))

left_dist = (left_time - right_time) * c
right_dist = (right_time - left_time) * c

print("left dist = " + str(left_dist))
print("right dist = " + str(right_dist))

def getAngleFromTime(deltaT):
    return np.arccos(c * deltaT/l)

#pdb.set_trace()
'''
if (left_dist > right_dist) :
    distance = (right_time - left_time) * c
    angle = np.arccos(right_dist/l)
    angle_degrees = np.degrees(angle)
else:
    angle = np.arccos(left_dist/l)
    angle_degrees = np.degrees(angle)
'''

angle = getAngleFromTime(deltaT)
angle_degrees = np.degrees(angle)

#pdb.set_trace()

print("angle = " + str(angle))
print("angle (degrees) = " + str(angle_degrees))


win = GraphWin('Speaker Angle', 1000, 750)
origin = Point(win.getWidth()/2, win.getHeight() - 10)
origin.draw(win)

radius = win.getWidth()/2 - 50

cir = Circle(origin, radius)
cir.setWidth(5)
cir.draw(win)

endpoint = Point( origin.getX() + cir.getRadius() * np.cos(angle), origin.getY() - cir.getRadius() * np.sin(angle))

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