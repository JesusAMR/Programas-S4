#! /usr/bin/python

def foo(bar):
	return bar

var = foo(5)

class cFoo:
	def __init__(self):
		self.member = 1
	def getMember(self):
		return self.member
	def setMember(self, dt):
		self.member = dt

var = cFoo()
var.setMember(5)
a = var.getMember()
print a
