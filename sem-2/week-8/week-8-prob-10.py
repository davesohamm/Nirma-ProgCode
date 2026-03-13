# 25MCD005 - PROB - J - Chat Screenshots

from bisect import *
import sys
input = sys.stdin.readline

for _ in '.' * int(input()):
    n, k = map(int, input().split())
    G = [set() for _ in range(n + 1)]
    I = [0] * (n + 1)

    for _ in range(k):
        a = [*map(int, input().split())]
        for a, b in zip(a[1:], a[2:]):
            if b not in G[a]:
                G[a].add(b)
                I[b] += 1

    Q = [i for i in range(1, n + 1) if I[i] == 0]
    C = 0

    for x in Q:
        C += 1
        for y in G[x]:
            I[y] -= 1
            if I[y] == 0:
                Q.append(y)

    print("YES" if C == n else "NO")