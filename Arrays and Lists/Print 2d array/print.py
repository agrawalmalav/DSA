from os import *
from sys import *
from collections import *
from math import *

n,m =[ int(x) for x in input().split()]
arr = []
for i in range(n):
    row = input()
    for x in range(n-i):
        print(row)


