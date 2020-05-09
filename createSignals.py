import numpy as np
import math
import pandas as pd
import pdb
import os

#define constants
f = 1000.0
c = 343
speaker_angle = 120
mic_distance = .1
t0 = 0.0
tf = 1e-3
step = 5e-6
n = (tf - t0) / step

def adc(analog):
    analogHigh = 5
    digitalHigh = 1023
    return int(analog * digitalHigh / analogHigh)

def getPhaseDiffFromAngle(angle):
    delta_t = mic_distance * np.cos(np.radians(speaker_angle)) / c
    return 2 * math.pi * delta_t * f

#initialize arrays to store the data
left_signal = np.zeros(int(n))
right_signal = np.zeros(int(n))
time = np.zeros(int(n))

#sample the sinusoid at a certain rate and store the values in an array
for i in range(int(n)):
    t = t0 + i * step
    time[i] = format(t, '.6g') #limit significant figures
    phase_diff = getPhaseDiffFromAngle(speaker_angle)
    
    left_signal[i] = adc(2.5 * np.cos(2*math.pi*f*t - phase_diff/2) + 2.5)
    right_signal[i] = adc(2.5 * np.cos(2*math.pi*f*t + phase_diff/2) + 2.5)

#now all sinusoid values in two arrays
#write arrays to file
left_table = pd.DataFrame({'time':time, 'signal':left_signal})
right_table = pd.DataFrame({'time':time, 'signal':right_signal})

test_case_dir = os.path.join(os.getcwd(), 'test_cases', str(speaker_angle))

os.mkdir(test_case_dir)

left_filepath = os.path.join(test_case_dir, 'left_signal.txt')
right_filepath = os.path.join(test_case_dir, 'right_signal.txt')

left_table.to_csv(left_filepath, index=False)
right_table.to_csv(right_filepath, index=False)


