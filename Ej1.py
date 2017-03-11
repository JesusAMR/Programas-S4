#! /usr/bin/python

input = raw_input("String: ")
#input = "Hello"
if len(input) > 2:
	print(input[2:]+ input[:2])
