from graphics import *
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import pdb

#define constants
c = 343.0
l = .1
T = 1e-3

#helper function 
def getAngleFromTime(deltaT):
    return np.arccos(c * deltaT/l)

#change this value to try different test cases
#note that this value is NOT the value which is displayed but just to point to the 
#correct data file
TEST_CASE = '120'

#READ DATA
left_filepath = os.path.join('test_cases', TEST_CASE, 'left_signal.txt')
right_filepath = os.path.join('test_cases', TEST_CASE, 'right_signal.txt')

table = pd.read_csv(left_filepath)
table.rename(columns={'signal':'left'}, inplace=True)
table2 = pd.read_csv(right_filepath)

table = table.join(table2['signal'])
table.rename(columns={'signal':'right'}, inplace=True)


#CALCULATE ANGLE FROM DATA
left_min_index = table['left'].idxmin()
right_min_index = table['right'].idxmin()

time_interval = T / len(table.index)

left_time = table.loc[left_min_index, 'time']
right_time = table.loc[right_min_index, 'time']
deltaT = left_time - right_time

angle = getAngleFromTime(deltaT)
angle_degrees = np.degrees(angle)


#DISPLAY DATA ON GUI
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

