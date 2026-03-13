# 25MCD005 - PROB - C
import sys
input = sys.stdin.readline

n = int(input())

dpA = dpB = dpC = 0

for _ in range(n):
    a, b, c = map(int, input().split())
    
    newA = a + max(dpB, dpC)
    newB = b + max(dpA, dpC)
    newC = c + max(dpA, dpB)
    
    dpA, dpB, dpC = newA, newB, newC

print(max(dpA, dpB, dpC))