def printPairDiffK(l, k):
    dic = {}
    for el in l:
        dic[el] = dic.get(el,0) +1
    ans = 0
    if k == 0:
        return len(l)*(len(l) -1) //2
    for el in l:
        if dic.get(el, 0) >0:
            ans += dic.get(el+k,0)*dic.get(el,0)
            ans += dic.get(el-k,0)*dic.get(el,0)
            del dic[el] 
    return ans




# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
print(printPairDiffK(l, k))
