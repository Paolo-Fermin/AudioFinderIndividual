import numpy as np
import math
import pandas as pd
import pdb

f = 1000.0
c = 343
speaker_angle = 45
mic_distance = .1

def adc(analog):
    analogHigh = 5
    digitalHigh = 1023
    return int(analog * digitalHigh / analogHigh)

def getPhaseDiffFromAngle(angle):
    delta_t = mic_distance * np.cos(np.radians(speaker_angle)) / c
    return 2 * math.pi * delta_t * f

t0 = 0.0
tf = 1e-3
step = 5e-6

n = (tf - t0) / step

#initialize arrays to store the data
left_signal = np.zeros(int(n))
right_signal = np.zeros(int(n))
time = np.zeros(int(n))

for i in range(int(n)):
    t = t0 + i * step
    time[i] = format(t, '.6g') #limit significant figures
    phase_diff = getPhaseDiffFromAngle(speaker_angle)
    
    #pdb.set_trace()

    left_signal[i] = adc(2.5 * np.cos(2*math.pi*f*t - phase_diff/2) + 2.5)
    right_signal[i] = adc(2.5 * np.cos(2*math.pi*f*t + phase_diff/2) + 2.5)

    '''
    if speaker_angle < 90: 
        left_signal[i] = adc(2.5 * np.cos(2*math.pi*f*t) + 2.5)
        right_signal[i] = adc(2.5 * np.cos(2*math.pi*f*t + phase_diff) + 2.5)
    else:
        left_signal[i] = adc(2.5 * np.cos(2*math.pi*f*t + phase_diff) + 2.5)
        right_signal[i] = adc(2.5 * np.cos(2*math.pi*f*t) + 2.5)
    '''
#array now has all sinusoid values in two arrays
#write arrays to file
left_table = pd.DataFrame({'time':time, 'signal':left_signal})
right_table = pd.DataFrame({'time':time, 'signal':right_signal})

left_table.to_csv('left_signal.txt', index=False)
right_table.to_csv('right_signal.txt', index=False)


