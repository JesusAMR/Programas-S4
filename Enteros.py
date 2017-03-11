#! /usr/bin/python

import math

romanosD =	{ "X":	1, "C":	2, "M":	3, "I":	0	}

romanosC =	{ "V":	0, "L":	1, "D":	2	}

entrada = raw_input("Inserte el numero: ")
class Decimales:

	def __init__(self):
		self.sum = 0
	def calcular(self, inpu):
		entrada = inpu  
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
		return sum

x = Decimales()
print(x.calcular(entrada))
