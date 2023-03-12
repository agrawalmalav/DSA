def permutations(string):
    if len(string) == 1:
        return [string]
    
    char = string[0]
    ans = permutations(string[1:])
    #print('ans', ans)
    newAns = []
    for s in ans:
        for i in range(len(s)+1):
            newAns.append(s[:i] + char + s[i:])
    return newAns
    
#main
string = input()
ans = permutations(string)
for s in ans:
    print(s)
    
