#! /usr/bin/python

import re

val = 0
operadores = "()^*/+-"
jerOperadores = {
					'(': 5,
					'^': 4,
					'*': 2,
					'/': 2,
					'+': 1,
					'-': 1
				}
jerPilaOp = {
				'^':3,
				'*':2,
				'/':2,
				'+':1,
				'-':1,
				'(':0
			}

def infija_postfija(inf):
	error = 0
	stack = []
	tmpInf = inf[::-1]
	tmpPost = []
	while(len(tmpInf) != 0 and (error != 1)):
		e = tmpInf.pop()
		print(e)
		if(e.isdigit()):
			tmpPost.append(int(e))
		elif(e == '('):
			stack.append(e)
		elif(e == ')'):
			print(stack)
			while(len(stack) != 0 and (stack[-1:] != '(' ) ):				
				tmpPost.append(stack.pop())
				print("StackL: ")
				print(stack)
				print("ListaL: ")
				print(tmpPost)
			print(stack)
			if(stack[-1:] == '('):
				stack.pop()
			else:
				error = 1
				break
		elif(e in operadores):
			while(len(stack) != 0 and ( jerOperadores[stack[-1]] >= jerOperadores[e] )):
				tmpPost.append(stack.pop())
			stack.append(e)
		print("Stack: ")
		print(stack)
		print("Lista: ")
		print(tmpPost)
	while(stack):
		tmpPost.append(stack.pop())
	stack = []
	print(error)
	return tmpPost

while(val == 0):
	input = raw_input()
	result = re.findall(r"([0-9]+[/.]?[0-9]+)*|[()^*/+-]",input)
	#result.pop()
	print(result)
	val = 1
	for i in result:
		if(i == ''):
			print "Cadena Invalida, vuelva a intentar"
			val = 0
			break
print(infija_postfija(result))
print(result)
