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

def subsets(arr, output):
    
    if len(arr) !=1:
        subOutput = subsets(arr[1:], output)
    else:
        subOutput = output
    n = len(subOutput)
    for i in range(n):
        temp = list(subOutput[i])
        temp.insert(0, arr[0])
        subOutput.append(temp)
    return subOutput

    





# main
n = int(input())
arr = [int(i) for i in input().split()]
output = [[]]
ans = subsets(arr, output)

for ss in ans:
    for ele in ss:
        print(ele, end= ' ')
    print()
