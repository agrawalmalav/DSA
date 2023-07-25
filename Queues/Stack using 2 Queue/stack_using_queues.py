
from sys import stdin

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack :

	#Define data members and __init__()
	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0



	'''----------------- Public Functions of Stack -----------------'''


	def getSize(self) :
		#Implement the getSize() function
		return self.count


	def isEmpty(self) :
		#Implement the isEmpty() function
		return self.count == 0


	def push(self, data) :
		#Implement the push(element) function
		node = Node(data)
		if self.head == None:
			self.head= node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node
		self.count += 1
		return


	def pop(self) :
		#Implement the pop() function
		if self.head == None:
			return -1
		else:
			if self.head == self.tail:
				data = self.head.data
				self.head =None
				self.tail = None
			else:
				prev = self.head
				while prev.next != self.tail:
					prev = prev.next
				data = prev.next.data
				self.tail = prev
				prev.next = None
			self.count -=1
			return data


	def top(self) :
		#Implement the top() function
		if self.tail != None:
			return self.tail.data
		else:
			return -1

		




#main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

	inputs = stdin.readline().strip().split(" ")
	choice = int(inputs[0])

	if choice == 1 :
		data = int(inputs[1])
		stack.push(data)

	elif choice == 2 :
		print(stack.pop())

	elif choice == 3 :
		print(stack.top())

	elif choice == 4 : 
		print(stack.getSize())

	else :
		if stack.isEmpty() :
			print("true")
		else :
			print("false")

	q -= 1
