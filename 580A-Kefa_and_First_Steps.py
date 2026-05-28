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

n = int1()

a = ints()

qtd = 1
maior = 0

for i in range(1, len(a), 1):
    if a[i] < a[i-1]:
        maior = max(maior, qtd)
        qtd = 0
    qtd += 1

print(max(maior, qtd))