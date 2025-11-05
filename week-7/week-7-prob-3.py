# 25MCD005 SOHAM DAVE WEEK-7 PROBLEM-3 "Party"
import sys

sys.setrecursionlimit(2005)

n = int(sys.stdin.readline())
managers = []
for _ in range(n):
    p = int(sys.stdin.readline())
    if p == -1:
        managers.append(-1)
    else:
        managers.append(p - 1)

depths = [0] * n

def get_depth(i):
    if depths[i] != 0:
        return depths[i]
    
    if managers[i] == -1:
        depths[i] = 1
        return 1
    
    manager_i = managers[i]
    depths[i] = get_depth(manager_i) + 1
    return depths[i]

max_depth = 0
for i in range(n):
    max_depth = max(max_depth, get_depth(i))

print(max_depth)
