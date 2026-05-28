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

MOD = 1000000007

t, k = map(int, input().split())

queries = []
max_b = 0

for _ in range(t):
    a, b = map(int, input().split())
    queries.append((a, b))
    max_b = max(max_b, b)

dp = [0] * (max_b + 1)
prefix = [0] * (max_b + 1)

dp[0] = 1

for i in range(1, max_b + 1):
    dp[i] = dp[i - 1]
    if i >= k:
        dp[i] = (dp[i] + dp[i - k]) % MOD

for i in range(1, max_b + 1):
    prefix[i] = (prefix[i - 1] + dp[i]) % MOD

for a, b in queries:
    ans = prefix[b] - (prefix[a - 1] if a > 0 else 0)
    print(ans % MOD)