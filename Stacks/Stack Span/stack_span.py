
from sys import stdin

def stockSpan(price, n) :
	#Your code goes here
	ans = [1]
	stack = [0]

	if n==1:
		return ans
	else:

		for i in range(1, n):
			while True:
				if len(stack)==0:
					ans.append(i+1)
					stack.append(i)
					break
				elif price[stack[-1]] >=price[i]:
					ans.append(i - stack[-1] )
					stack.append(i)
					break
				else:
					stack.pop()
		return ans


'''-------------- Utility Functions --------------'''




def printList(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = " ")

	print()


def takeInput():
	size = int(stdin.readline().strip())

	if size == 0 :
		return list(), 0

	price = list(map(int, stdin.readline().strip().split(" ")))

	return price, size


#main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)
