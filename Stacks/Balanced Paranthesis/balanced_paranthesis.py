
from sys import stdin


def isBalanced(expression) :
	#Your code goes here
	stack = []

	for ele in expression:
		if ele == "(":
			stack.append(ele)
		elif ele == ')':
			if len(stack) == 0 or stack[-1] == ')':
				return False
			else:
				stack.pop()
		#print(stack)
	
	if len(stack) != 0:
		return False
	else:
		return True


#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")
