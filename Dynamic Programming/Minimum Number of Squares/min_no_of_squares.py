

import sys
sys.setrecursionlimit(10**6)

def minStepsTo1(n, arr):
    #Implement Your Code Here
    #approach1 - Recurrsion
    '''
    if n==0:
        arr[n] = 0
        return 0
    i =1
    ans = n-1
    while i*i <= n:
        if arr[n-i*i] == -1:
            arr[n-i*i] = minStepsTo1(n-i*i, arr)
        ans = min(ans, arr[n-i**2])
        i+=1
    return 1+ ans
    '''
    #approach2 - Iterative
    arr[0] = 0
    i=1
    while i<=n:
        j=1
        ans = i
        while j**2 <=i:
            currAns = arr[i-j**2]
            ans=  min(ans, currAns+1)
            j+=1
        arr[i] = ans
        i+=1
        #print(arr)
    return arr[n]
        
    

        

    
n = int(input())
arr = [-1 for i in range(n+1)]
ans = minStepsTo1(n, arr)
print(ans)





