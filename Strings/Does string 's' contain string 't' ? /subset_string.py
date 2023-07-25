def contains(s,t):
    #Implement This Function Here
    i, j =0,0
    while True:
        if j == len(t):
            return True
        elif j< len(t) and i == len(s):
            return False

        if s[i] != t[j]:
            i+=1
        elif s[i] == t[j]:
            i+=1
            j+=1


    
s = input()
t = input()

ans = contains(s,t)
if ans is True:
    print('true')
else:
    print('false')
