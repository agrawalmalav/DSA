from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.

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
