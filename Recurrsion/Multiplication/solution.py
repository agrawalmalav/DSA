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
def recMul(n,m):
    if m ==0:
        return 0
    return recMul(n, m-1) + n

n = int(input())
m= int(input())

if n< m:
    n,m = m,n
print(recMul(n,m))
