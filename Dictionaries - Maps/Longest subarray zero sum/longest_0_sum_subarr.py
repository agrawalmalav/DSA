def subsetSum(l):
    maxLen = 0
    dic = {}
    sum = 0
    for i in range(len(l)):
        sum +=l[i]
        if sum == 0:
            if i > maxLen:
                maxLen = i+1
        if sum in dic:
            if i - dic[sum] > maxLen:
                maxLen = i- dic[sum]
        else:
            dic[sum] = i
        #print(dic)

    return maxLen
            



# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))
