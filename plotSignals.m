signal1 = readmatrix("signal1.txt");
signal2 = readmatrix("signal2.txt");

period = 1*10^-3;
increment = period / length(signal1);
time = 0:increment:period-increment;

plot(angle(Y1));

figure;
hold on;
grid;
title('Signals from two mics');
xlabel('time (s)');
ylabel('DC value (0-1024)');
plot(time, signal1);
plot(time, signal2);
hold off;