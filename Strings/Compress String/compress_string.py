from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)


def getCompressedString(string) :
	# Write your code here.
	curr = ''
	count = 1
	ans = ''

	for i in range(len(string)-1):
		if string[i] != string[i+1]:
			ans += string[i]
			if count > 1:
				ans += str(count)
			count = 1
		else:
			count +=1
	ans += string[-1]
	if count>1:
		ans += str(count) 
	return ans




# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)
