# Write your code here...
def strToInt(string):
    if len(string) ==0:
        return 0

    return strToInt(string[:len(string)-1])*10 + ord(string[-1]) - ord('0')


string = input()
print(strToInt(string))
