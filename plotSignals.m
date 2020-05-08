clear;
clc;
close all;

left_signal = readmatrix("left_signal.txt");
right_signal = readmatrix("right_signal.txt");

period = 1*10^-3;
increment = period / length(left_signal);
time = 0:increment:period-increment;

figure;
hold on;
grid;
title('Signals from two mics');
xlabel('time (s)');
ylabel('DC value (0-1024)');
left_plot = plot(time, left_signal, 'DisplayName', 'left');
right_plot = plot(time, right_signal, 'DisplayName', 'right');
legend();
hold off;