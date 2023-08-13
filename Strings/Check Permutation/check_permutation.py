
from sys import stdin


def isPermutation(string1, string2) :
	#Your code goes here
    '''
    str2 = list(string2)
    for x in string1:
        if x in str2:
            str2.remove(x)
        else:
            return False
    return True
'''
    if len(string1) != len(string2):
        return False
    freq = [0]*26
    for i in range(len(string1)):
        freq[ord(string1[i])-ord('a')] += 1
        freq[ord(string2[i])-ord('a')] -= 1
    if freq != [0]*26:
        return False
    else:
        return True

#main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')

