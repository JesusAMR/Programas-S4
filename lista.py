#! /usr/bin/python

lista = raw_input("Inserte la informacion: ")
nvlista = tuple(lista.split(','))

def conversion(lst):
	print(tuple(lst.split(',')))

conversion(lista)
#lista = tuple(raw_input("Inserte la informacion: ").split(','))


print(lista)
