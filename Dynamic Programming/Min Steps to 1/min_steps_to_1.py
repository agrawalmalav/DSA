import sys
#from sys import stdin
from sys import maxsize as MAX_VALUE

sys.setrecursionlimit(10**6)

def countMinStepsToOne(n, arr):
    #approach 1- recurrsion
    '''
    if arr[n] != -1:
        return arr[n]

    if n==1:
        arr[1] = 0
        return 0
    ans1 = n-1
    if n%3 ==0:
        if arr[n//3] == -1:
            ans1 = countMinStepsToOne(n//3, arr)
            arr[n//3] = ans1
        else:
            ans1 = arr[n//3]

    ans2 = n-1
    if n%2 ==0:
        if arr[n//2] == -1:
            ans2 = countMinStepsToOne(n//2, arr)
            arr[n//2] = ans2
        else:
            ans2 = arr[n//2]

    ans3 = n-1
    #print('ans3 before', ans3)
    #print('arr', arr)
    if arr[n-1] == -1 and n>1:
         ans3 = countMinStepsToOne(n-1, arr)
         arr[n-1] = ans3
         #print('ans3 if', ans3)
    elif n >1 :
        ans3 = arr[n-1]
        #print('ans3 else', ans3)
    #print(ans1, ans2, ans3)
    ans= 1+ min(ans1, ans2, ans3)
    return ans
    '''
    #approach2- iteration 
    arr[1] = 0
    for i in range(2, n+1):
        ans = arr[i-1]
        if i%2==0:
            ans= min(ans, arr[i//2])
        if i%3 == 0:
            ans = min(ans, arr[i//3])
        arr[i] = ans+1
    #print(arr)
    return arr[n]
    
    

#main
n = int(sys.stdin.readline().rstrip())
arr = [-1 for i in range(n+1)]
print(countMinStepsToOne(n, arr))
