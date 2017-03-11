#! /usr/bin/python

import sys
inp = raw_input("Inserte el numero: ")
class Romano:
	def __init__(self, entrada):
		self.lstnRom	=	{ 1: "I", 2: "X", 3: "C", 4:	"M"	}
		self.lstcRom	=	{	1: "V", 2: "L",	3: "D"}
		self.entrada	= entrada
		self.lon			= len(entrada)
		self.lim			= self.lon
		self.result		= ""
	def conversion(self):
		for i in xrange(0,self.lon):
			if ( int(self.entrada[i]) in range(1,4)):
				self.result = self.result + self.lstnRom[self.lon] * int(self.entrada[i])
				self.lon = self.lon - 1
			elif( int(self.entrada[i]) == 0):
				self.lon = self.lon - 1
			elif( int(self.entrada[i]) == 4):
				self.result = self.result + self.lstnRom[self.lon] + self.lstcRom[self.lon]
				self.lon = self.lon - 1
			elif( int(self.entrada[i]) == 5):
				self.result = self.result + self.lstcRom[self.lon]
				self.lon = self.lon - 1
			elif( int(self.entrada[i]) in range(6,9)):
				self.result = self.result + lstcRom[lon] + self.lstnRom[self.lon] * (int(self.entrada[i])-5)
				self.lon = self.lon - 1
			elif( int(self.entrada[i]) == 9):
				self.result = self.result + self.lstnRom[self.lon] + self.lstnRom[self.lon+1]
				self.lon = self.lon -1
		return self.result

x = Romano(inp)
print(x.conversion())
