#! /usr/bin/python

num = 311
numero = str(num)
lim =len(numero)
dicc = {
		"1": ["I", "V"],
		"2": ["X", "L"],
		"3": ["C", "D"]
		}
i = 0
romano = ""

while(lim != 0):
	if(numero[i] == "1" or numero[i] == "2" or numero[i] == "3"):
		romano = romano + str(dicc[str(lim)])[2] * int(numero[i])
		lim = lim-1
		i = i +1
	elif(numero[i] == "0"):
		lim = lim-1
		i = i+1

print(romano)
