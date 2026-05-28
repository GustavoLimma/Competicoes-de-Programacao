import sys
import math
import bisect
import heapq
from collections import *
from itertools import *

input = sys.stdin.readline

def ints():    
    return list(map(int, input().split()))

def int1():    
    return int(input())

def int2():
    return map(int, input().split())

#=========================================

MOD = 10**6 + 3

n = int1()

if n == 0:
    print(1)
else:
    print(pow(3, n - 1, MOD))