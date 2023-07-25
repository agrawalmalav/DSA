
def checkPalindrome(string):
    if len(string) ==0 or len(string) == 1:
        return True

    if string[0] != string[-1]:
        return False
    else:
        return checkPalindrome(string[1:len(string)-1])

string = input()
if checkPalindrome(string):
    print('true')
else:
    print('false')
