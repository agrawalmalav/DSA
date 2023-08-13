
from sys import stdin


def reverseEachWord(string) :
	# Your code goes here
	ans = ''
	words = string.split()
	for word in words:
		ans = ans + word[::-1] + " "
	return ans[:len(ans)-1]



#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)
