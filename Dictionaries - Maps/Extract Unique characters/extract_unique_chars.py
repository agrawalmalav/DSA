def uniqueChar(s): 
    # Write your code here
    dic = {}
    ans = ''
    for char in s:
        if dic.get(char,0) ==0:
            ans += char
            dic[char] = 1
        else:
            dic[char] +=1

    return ans



# Main 
s=input() 
print(uniqueChar(s))
