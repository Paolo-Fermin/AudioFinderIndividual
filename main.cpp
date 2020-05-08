#include<stdio.h>
#include<math.h>
#include <iostream>

#define pi 3.14159265
#define f 1000.0 // 1000 Hz signal
#define speedOfSound 343
#define speakerAngle 45
#define micLength .1
#define theta1 90 // phase angle LEFT
#define theta2 -85	//phase angle RIGHT

using namespace std;


int adc(float analog) {
	float analogLow = 0.0;
	float analogHigh = 5.0;
	float digitalLow = 0;
	float digitalHigh = 1023;
	int signal = int(analog * digitalHigh / analogHigh);
	cout << signal << endl;
	return signal;
}

float toRadians(int deg) {
	return (pi / 180) * deg;
}

float getPhaseDifferenceFromAngle(int angle) {
	float deltaT = micLength * cos(toRadians(angle)) / speedOfSound;
	cout << deltaT << endl;
	return 2 * pi * deltaT * f;
}

int main(void)
{
	double t0 = 0.0, tf = 1E-3, step = 5E-6, p1, p2, t; // tf is 1ms, step is sampling rate
	int i, n;
	FILE* output_file1;
	FILE* output_file2; // declare a pointer pointing to a file
	output_file1 = fopen("signal1.txt", "w"); // �w� is the argument for writing
	output_file2 = fopen("signal2.txt", "w");

	n = (tf - t0) / step; // samples from 0 to n-1
	for (i = 0; i < n; i++)
	{
		t = t0 + i * step;

		float phaseDifference = getPhaseDifferenceFromAngle(speakerAngle);
		cout << phaseDifference << endl;
		p1 = 2.5 * sin(2 * pi * f * t) + 2.5; // samples from 0 to n-1
		p2 = 2.5 * sin(2 * pi * f * t - phaseDifference) + 2.5; // samples from 0 to n-1

		fprintf(output_file1, "%d\n", adc(p1)); // write the samples into a file
		fprintf(output_file2, "%d\n", adc(p2));
	}
	if (output_file1)
	{
		fclose(output_file1); // to make sure file is accessible
		fclose(output_file2);
	}
	return 0;
}
