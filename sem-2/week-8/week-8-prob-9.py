# 25MCD005 - PROB - I - Nastya and Potions


import sys
input = sys.stdin.readline

def topo_order(graph):
    n = len(graph)
    in_deg = [0] * n

    for node in range(n):
        for nei in graph[node]:
            in_deg[nei] += 1

    reversed_topo = [node for node in range(n) if in_deg[node] == 0]

    for node in reversed_topo:
        for nei in graph[node]:
            in_deg[nei] -= 1
            if in_deg[nei] == 0:
                reversed_topo.append(nei)

    return reversed_topo[::-1]


for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    cost = [int(x) for x in input().split()]
    free_positions = [int(x) - 1 for x in input().split()]

    for node in free_positions:
        cost[node] = 0

    graph = [[int(x) - 1 for x in input().split()][1:] for _ in range(n)]

    topo = topo_order(graph)

    for node in topo:
        if not graph[node]:
            continue

        s = 0
        for nei in graph[node]:
            s += cost[nei]

        cost[node] = min(cost[node], s)

    print(*cost)