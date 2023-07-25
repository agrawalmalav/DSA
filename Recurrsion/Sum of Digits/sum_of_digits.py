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

def sumOfDigits(n):
    if n//10 == 0:
        return n

    return n%10 + sumOfDigits(n//10)


n = int(input())
print(sumOfDigits(n))
