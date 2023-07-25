
from sys import stdin

def countBracketReversals(inputString) :
    # Your code goes here
    stack = []
    count = 0
    for x in inputString:
        if x == '{':
            stack.append(x)
        if x == '}':
            if len(stack) !=0:
                stack.pop()
            else:
                count += 1
                stack.append('{')

    if len(stack) %2 ==1:
        return -1
    else:
        return len(stack)//2 +count
        


#main
print(countBracketReversals(stdin.readline().strip()))
