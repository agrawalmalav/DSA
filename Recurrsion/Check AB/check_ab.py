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

def checkAB(string):
    if len(string) ==1 and string[0] =='a':
        return True
    elif len(string) ==2 and string == 'bb':
        return True

    if string[0] =='a' and (string[1:3] =='bb' or string[1] =='a'):
        return checkAB(string[1:])
    elif string[:2] =='bb' and string[2] =='a':
        return checkAB(string[2:])
    else:
        return False


string = input()
if string[0] != 'a':
    print('false')
elif checkAB(string):
    print('true')
else:
    print('false')
