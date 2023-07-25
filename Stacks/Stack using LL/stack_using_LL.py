
from sys import stdin

#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Stack :

    #Define data members and __init__()
    def __init__(self):
        self.__head = None
        self.__count = 0




    '''----------------- Public Functions of Stack -----------------'''


    def getSize(self) :
        #Implement the getSize() function
        return self.__count



    def isEmpty(self) :
        #Implement the isEmpty() function
        if self.__count ==0:
            return True
        else:
            return False



    def push(self, data) :
        #Implement the push(element) function
        node = Node(data)
        if self.__head == None:
            self.__head = node
        else:
            node.next = self.__head
            self.__head = node
        self.__count +=1
        return




    def pop(self) :
        #Implement the pop() function
        if self.__count == 0:
            ele = -1
        else:
            ele = self.__head.data
            self.__count -=1
        if self.__head != None:
            self.__head = self.__head.next
        
        return ele


    def top(self) :
        #Implement the top() function
        if self.__count == 0:
            return -1
        else:
            return self.__head.data
        
        




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
