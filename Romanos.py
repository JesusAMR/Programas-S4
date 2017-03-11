#! /usr/bin/python
import sys
#inp = raw_input("Inserte el numero: ")

def cal(entrada):
  lstnRom =	{
			  1:	"I",
			  2:	"X",
			  3:	"C",
			  4:	"M"
			  }

  lstcRom =	{
			  1: "V",
			  2: "L",
			  3: "D"
			  }
  lon = len(entrada)
  lim = lon
  result = ""
  for i in xrange(0,lon):
	  numActual = int(entrada[i])
	  if ( int(entrada[i]) in range(1,4)):
		  result = result + lstnRom[lon] * int(entrada[i])
		  lon = lon - 1
	  elif( int(entrada[i]) == 0):
		  lon = lon - 1
	  elif( int(entrada[i]) == 4):
		  result = result + lstnRom[lon] + lstcRom[lon]
		  lon = lon - 1
	  elif( int(entrada[i]) == 5):
		  result = result + lstcRom[lon]
		  lon = lon - 1
	  elif( int(entrada[i]) in range(6,9)):
		  result = result + lstcRom[lon] + lstnRom[lon] * (int(entrada[i])-5)
		  lon = lon - 1
	  elif( int(entrada[i]) == 9):
		  result = result + lstnRom[lon] + lstnRom[lon+1]
		  lon = lon -1
  sys.stdout.write(result)
  sys.stdout.flush()

for i in range(1,600):
	cal(str(i))
	print(" ")
