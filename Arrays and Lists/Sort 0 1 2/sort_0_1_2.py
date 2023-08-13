from sys import stdin 

def sort012(arr, n) :
    #Your code goes here
    # basic approach
    '''
    count0, count1, count2 = 0,0,0
    for x in arr:
        if x==0:
            count0+=1
        elif x ==1:
            count1 +=1
        else:
            count2 +=1
    arr[0:count0] = [0]*count0
    arr[count0: count0+count1] = [1]* count1
    arr[(count0+count1):] = [2]*count2
    '''
    #better approach
    nz =0
    nt = n-1
    i=0
    while i<n and i <=nt:
        #print('ele: ', arr[i])
        if arr[i] == 0:
            arr[i], arr[nz] = arr[nz], arr[i]
            i+=1
            nz+=1
        elif arr[i] ==2:
            arr[nt], arr[i] = arr[i], arr[nt]
            nt -=1
        else:
            i+=1
        #print(arr)



#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()

    sort012(arr, n)
    printList(arr, n)
    
    t -= 1
