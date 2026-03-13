# 25MCD005 SOHAM DAVE WEEK-8 PROBLEM-2 "Bear and Friendship Condition"
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
adj = [set() for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].add(b)
    adj[b].add(a)

visited = set()
is_reasonable = True
for i in range(1, n + 1):
    if i not in visited:
        component_nodes = []
        q = deque([i])
        visited.add(i)
        
        while q:
            u = q.popleft()
            component_nodes.append(u)
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        
        k = len(component_nodes)
        component_edges = 0
        for u in component_nodes:
            component_edges += len(adj[u])
        
        component_edges //= 2
        
        if component_edges != k * (k - 1) // 2:
            is_reasonable = False
            break

if is_reasonable:
    print("YES")
else:
    print("NO")
