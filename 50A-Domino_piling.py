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

m, n = int2()

print(int((m*n)/2))