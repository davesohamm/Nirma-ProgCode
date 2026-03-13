# 25MCD005 - PROB - G
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    indegree[y] += 1

q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

dp = [0]*(n+1)

while q:
    u = q.popleft()
    for v in graph[u]:
        dp[v] = max(dp[v], dp[u] + 1)
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

print(max(dp))