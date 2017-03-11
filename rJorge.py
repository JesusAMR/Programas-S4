#! /usr/bin/python

num = raw_input("Ingrese un numero para convertir a romano: ")
numero = str(num)
lim =len(numero)
dicc = {
		#Formato [1 , 5]
		#        [1*10, 5*10]
		#		 [10*10, 50*10]
		#        ......
		"1": ["I", "V"],
		"2": ["X", "L"],
		"3": ["C", "D"],
		"4": ["M", "v"]
		}
i = 0
romano = ""

chain =  str(dicc[str(lim)])[1]

while(lim != 0):
	if(numero[i] == "1" or numero[i] == "2" or numero[i] == "3"):
		romano = romano + dicc[str(lim)][0] * int(numero[i])
		lim = lim - 1
		i = i + 1
	elif(numero[i] == "6" or numero[i] == "7" or numero[i] == "8"):
		romano = romano + dicc[str(lim)][1] + dicc[str(lim)][0] * (int(numero[i]) - 5)
		lim = lim - 1
		i = i + 1
	elif(numero[i] == "5"):
		romano = romano + dicc[str(lim)][1]
		lim = lim - 1
		i = i + 1
	elif(numero[i] == "4"):
		romano = romano + dicc[str(lim)][0] + dicc[str(lim)][1]
		lim = lim - 1
		i = i + 1
	elif(numero[i] == "9"):
		romano = romano + dicc[str(lim)][0] + dicc[str(lim + 1)][0]
		lim = lim - 1
		i = i + 1
	elif(numero[i] == "0"):
		lim = lim - 1
		i = i + 1
print(romano)