
from sys import stdin


def highestOccuringChar(string) :
	#Your code goes here
	freq = [0]*26
	for x in string:
		freq[ord(x) - ord('a')] += 1
	idx = freq.index(max(freq))
	return chr(idx+ord('a'))

#main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)
