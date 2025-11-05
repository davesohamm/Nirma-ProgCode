# 25MCD005 SOHAM DAVE WEEK-7 PROBLEM-5 "Bmail Computer Network"
import sys

def solve():
    n = int(sys.stdin.readline())
    
    if n == 1:
        print(1)
        return

    p_values = list(map(int, sys.stdin.readline().split()))
    
    parent = [0] * (n + 1)
    
    for i in range(n - 1):
        parent[i + 2] = p_values[i]
        
    path = []
    curr = n
    while curr != 0:
        path.append(curr)
        curr = parent[curr]
        
    path.reverse()
    
    print(*path)

solve()
