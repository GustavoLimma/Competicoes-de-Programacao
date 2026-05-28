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

a = int1()

qtd = 0
lista = []

for i in range(a):
    a1, a2 = int2()
    lista.append(a1 - a2)
    if abs(lista[i]) >= 2:
        qtd +=1

print(qtd)