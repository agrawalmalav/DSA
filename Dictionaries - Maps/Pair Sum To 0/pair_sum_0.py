from sys import stdin

def pairSum0(l,n):
    # Write your code here
    dic = {}
    for el in l:
        dic[el] = dic.get(el,0) +1
    #print(dic)
    ans = 0 
    for el in dic:
        if -el in dic and el!=0:
            ans += dic[el] * dic[-el]
            dic[el] =0
            dic[-el] =0
        elif el == 0:
            ans += (dic[el]*(dic[el]-1))//2
            dic[el] = 0
    return ans
                
    
    '''
        if el != 0:
            ans += dic.get(el)*dic.get(-el, 0)
    return ans//2 + dic.get(0,0)*2
    '''









    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(pairSum0(arr,n))
