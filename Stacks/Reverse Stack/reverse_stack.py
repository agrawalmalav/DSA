from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


def reverseStack(inputStack, extraStack) :
	#Your code goes here
	if len(inputStack) == 0 or len(inputStack) == 1:
		return

	n = len(inputStack)
	for i in range(n-1):
		extraStack.append(inputStack.pop())
	top = inputStack.pop()

	for i in range(n-1):
		inputStack.append(extraStack.pop())

	reverseStack(inputStack, extraStack)
	inputStack.append(top)

	


'''-------------- Utility Functions --------------'''

#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Taking input using fast I/o method
def takeInput() :
	size = int(stdin.readline().strip())
	inputStack = list()

	if size == 0 :
		return inputStack


	values = list(map(int, stdin.readline().strip().split(" ")))
	inputStack = values

	return inputStack


# Main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack) :
	print(inputStack.pop(), end = " ")
