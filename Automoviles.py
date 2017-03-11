#! /usr/bin/python

from Auto import Vehiculo

class Auto(Vehiculo):
	def Arrancar(self):
		print("Metodo Arrancar de la clase hija Auto")

class Camion(Vehiculo):
	def Arrancar(self):
		print("Metodo Arrancar de la clase hija Camnion")

