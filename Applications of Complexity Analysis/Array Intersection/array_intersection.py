from sys import stdin


def intersection(arr1, arr2, n, m) :
	#Your code goes here
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    #print(arr1)
    #print(arr2)

    i, j=0,0
    ans = []
    while i<len(arr1) and j< len(arr2):
        #print('arr1', arr1[i], 'arr2', arr2[j])
        if arr1[i] == arr2[j]:
            ans.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i] > arr2[j]:
            j+=1
        else:
            i+=1
        #print(ans)
    for x in ans:
        print(x, end= ' ' )



























# Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
    	return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()
    intersection(arr1, arr2, n, m)
    print()

    t -= 1
