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
n = int(input())
arr = [int(x) for x in input().split()]
x = int(input())

#passing the arry
'''
def lastIdx(arr, x):

    if len(arr) == 0:
        return -1

    sub_prob = lastIdx(arr[1:], x)
    if sub_prob == -1:
        if arr[0] ==x:
            return 0
        else:
            return -1
    else:
        return sub_prob + 1
'''
'''
#passing idx
def lastIdx(arr, x, curr_idx = 0, ans = -1):

    if curr_idx == len(arr):
        return ans

    if arr[curr_idx] == x:
        ans = curr_idx
    return lastIdx(arr, x, curr_idx+1, ans)  
'''
#passing index better
def lastIdx(arr, x, idx = 0):

    if idx == len(arr):
        return -1

    sub_ans = lastIdx(arr,x, idx+1)
    if sub_ans !=-1:
        return sub_ans
    else:
        if arr[idx] ==x:
            return idx
        else:
            return -1
    





print(lastIdx(arr, x))

