#! /usr/bin/python

import sys

"""
	Write a Python program to accept a filename from the user and print the extension of that.
	Sample filename : abc.java
	Output : java
"""


posPunto = sys.argv[-1].find(".")

print "La extencion del archivo es : "+ sys.argv[-1][posPunto+1:]
