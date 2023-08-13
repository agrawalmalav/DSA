from sys import stdin

def removeConsecutiveDuplicates(string) :
	# Your code goes here
	'''
	ans= ''
	i = 0
	last =''
	while i < len(string):
		if last != string[i]:
			last = string[i]
			ans += last
		i+=1
	return ans
	'''

	ans= ''
	for i in range(len(string)-1):
		if string[i] != string[i+1]:
			ans += string[i]
	ans += string[-1]
	return ans



#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)
