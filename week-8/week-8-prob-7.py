# 25MCD005 SOHAM DAVE WEEK-8 PROBLEM-7 "Shortest Routes I"
import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))

dist = [float('inf')] * (n + 1)
pq = []

dist[1] = 0
heapq.heappush(pq, (0, 1))

while pq:
    d, u = heapq.heappop(pq)

    if d > dist[u]:
        continue

    for v, weight in adj[u]:
        if dist[u] + weight < dist[v]:
            dist[v] = dist[u] + weight
            heapq.heappush(pq, (dist[v], v))

output = " ".join(map(str, dist[1:]))
sys.stdout.write(output + "\n")

