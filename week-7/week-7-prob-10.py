# 25MCD005 SOHAM DAVE WEEK-7 PROBLEM-10 "Choosing Capital for Treeland"
import sys
from collections import deque

sys.setrecursionlimit(200010)

n = int(sys.stdin.readline())

if n == 1:
    print(0)
    print(1)
    sys.exit()

adj = [[] for _ in range(n)]
directed_edges = set()

for _ in range(n - 1):
    s, t = map(int, sys.stdin.readline().split())
    s -= 1
    t -= 1
    adj[s].append(t)
    adj[t].append(s)
    directed_edges.add((s, t))

cost = [0] * n
parent = [-1] * n

q = deque([0])
nodes_in_bfs_order = []
visited = [False] * n
visited[0] = True

while q:
    u = q.popleft()
    nodes_in_bfs_order.append(u)
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            q.append(v)

initial_cost = 0
for u in nodes_in_bfs_order[1:]:
    p = parent[u]
    if (u, p) in directed_edges:
        initial_cost += 1

cost[0] = initial_cost

for u in nodes_in_bfs_order[1:]:
    p = parent[u]
    if (p, u) in directed_edges:
        cost[u] = cost[p] + 1
    else:
        cost[u] = cost[p] - 1

min_cost = min(cost)
result_nodes = []
for i in range(n):
    if cost[i] == min_cost:
        result_nodes.append(i + 1)
        
print(min_cost)
print(" ".join(map(str, result_nodes)))
