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

def geometricSum(k):
    if k ==0:
        return 1

    return geometricSum(k-1 ) + (1/2)**k

k = int(input())
ans = geometricSum(k)
print(format(ans, '.5f'))
