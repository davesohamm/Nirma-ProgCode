# 25MCD005 SOHAM DAVE WEEK-7 PROBLEM-6 "Subordinates"

import sys

n = int(sys.stdin.readline())

adj = [[] for _ in range(n)]

if n > 1:
    bosses = list(map(int, sys.stdin.readline().split()))
    for i in range(n - 1):
        employee_idx = i + 1
        boss_idx = bosses[i] - 1
        adj[boss_idx].append(employee_idx)

subordinate_counts = [0] * n

stack = []
post_order_nodes = []
visited = [False] * n

stack.append(0)

while stack:
    u = stack[-1]
    
    if not visited[u]:
        visited[u] = True
        for v in reversed(adj[u]):
            if not visited[v]:
                stack.append(v)
    else:
        stack.pop()
        post_order_nodes.append(u)

for u in post_order_nodes:
    count = 0
    for v in adj[u]:
        count += (1 + subordinate_counts[v])
    subordinate_counts[u] = count

sys.stdout.write(" ".join(map(str, subordinate_counts)) + "\n")

