
from sys import stdin

def checkRedundantBrackets(expression) :
	# Your code goes here
	stack = []
	for x in expression:
		if x != ')':
			stack.append(x)
		else:
			count = 0
			while stack[-1] != '(':
				count +=1
				stack.pop()
			stack.pop()
			if count <2:
				return True
	return False




#main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")
