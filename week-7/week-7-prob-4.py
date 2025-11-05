# 25MCD005 SOHAM DAVE WEEK-7 PROBLEM-4 "Tree Diameter"
import sys
from collections import deque

def solve():
    n = int(sys.stdin.readline())
    if n == 1:
        print(0)
        return

    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)

    def bfs(start_node):
        dist = [-1] * n
        dist[start_node] = 0
        q = deque([start_node])
        farthest_node = start_node
        max_dist = 0

        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
                    if dist[v] > max_dist:
                        max_dist = dist[v]
                        farthest_node = v
        
        return farthest_node, max_dist

    farthest_node_1, dist_1 = bfs(0)
    farthest_node_2, diameter = bfs(farthest_node_1)

    print(diameter)

solve()
