
a1 = []
a2= []

def split(arr,i =0,sum5=0, sum3=0):
    #Implement Your Function here
    if sum(arr) %2 ==1:
        return False
    else:
        if i == len(arr):
            return sum5==sum3
        else:
            if arr[i] %5==0:
                sum5 += arr[i]
                return split(arr, i+1, sum5, sum3)
            elif arr[i] %3 == 0:
                sum3 += arr[i]
                return split(arr, i+1, sum5, sum3)
            else:
                return  split(arr, i+1, sum5+arr[i] , sum3) or split(arr, i+1, sum5, sum3+ arr[i])

    
    
n = input()
arr = [int(ele) for ele in input().split()]
ans = split(arr)
if ans is True:
    print('true')
else:
    print('false')
