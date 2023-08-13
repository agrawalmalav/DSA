
from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
	# Your code goes here
	ans =''
	for x in string:
		if x!= ch:
			ans += x
	return ans


#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)
