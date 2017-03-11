#! /usr/bin/python

import math

f1 = open('Romanos.txt', 'r')
f2 = open('Numeros.txt', 'w')

romanosD =	{
						"X":	1,
						"C":	2,
						"M":	3,
						"I":	0
						}

romanosC =	{
						"V":	0,
						"L":	1,
						"D":	2
						}

#entrada = raw_input("Inserte el numero: ")
for line in f1:
	entrada = line  
	long	= len(entrada)
	sum 	= 0
	i 		= 0
	while(i != long):
		if(i+1 < long and entrada[i+1] in romanosD and entrada[i] in romanosD and romanosD[entrada[i]] < romanosD[entrada[i+1]]):
			sum = sum + pow(10, romanosD[entrada[i+1]]) - pow(10, romanosD[entrada[i]])
			i = i + 1
		elif(i+1 < long and entrada[i+1] in romanosC and entrada[i] in romanosD and romanosD[entrada[i]]== romanosC[entrada[i+1]]):
			sum = sum + pow(10, romanosC[entrada[i+1]]) * 5 - pow(10, romanosD[entrada[i]])
			i = i + 1
		elif(entrada[i] in romanosD):
			sum = sum + pow(10, romanosD[entrada[i]])
		elif(entrada[i] in romanosC):
			sum = sum + pow(10, romanosC[entrada[i]]) * 5
		i = i + 1

	f2.write(str(sum) + '\n')
f1.close()
f2.close()

