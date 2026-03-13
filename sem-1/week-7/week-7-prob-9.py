# 25MCD005 SOHAM DAVE WEEK-7 PROBLEM-9 "Tree Queries"
import sys

def solve():
    try:
        sys.setrecursionlimit(200010)
    except (ImportError, ValueError):
        pass

    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    timer = 0

    def dfs(u, p, d):
        nonlocal timer
        tin[u] = timer
        timer += 1
        parent[u] = p
        depth[u] = d
        for v in adj[u]:
            if v != p:
                dfs(v, u, d + 1)
        tout[u] = timer
        timer += 1

    dfs(1, 1, 0)

    def is_ancestor(u, v):
        return tin[u] <= tin[v] and tout[v] <= tout[u]

    results = []
    for _ in range(m):
        line = list(map(int, sys.stdin.readline().split()))
        k = line[0]
        v = line[1:]

        max_parent_depth = -1
        v_cand = -1
        for node in v:
            if depth[parent[node]] > max_parent_depth:
                max_parent_depth = depth[parent[node]]
                v_cand = node

        if v_cand == -1:
            v_cand = v[0]
            
        u_cand = v_cand
        possible = True
        for w in v:
            if not (is_ancestor(w, u_cand) or is_ancestor(parent[w], u_cand)):
                possible = False
                break
        
        if possible:
            results.append("YES")
        else:
            results.append("NO")

    print('\n'.join(results))

solve()
