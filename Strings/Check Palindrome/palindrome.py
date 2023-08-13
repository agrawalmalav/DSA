
from sys import stdin


def isPalindrome(string) :
	# Your code goes here
    s, e = 0, len(string) -1
    while s<e:
        if string[s] != string[e]:
            return False
        s +=1
        e -=1
    return True


#main
string = stdin.readline().strip();
ans = isPalindrome(string)

if ans :
    print('true')
else :
    print('false')

