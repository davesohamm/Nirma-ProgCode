# 25MCD005 - PROB - F
import sys
input = sys.stdin.readline

n, W = map(int, input().split())

items = [tuple(map(int, input().split())) for _ in range(n)]

V = sum(v for _, v in items)

INF = 10**18
dp = [INF] * (V + 1)
dp[0] = 0

for w, v in items:
    for val in range(V, v-1, -1):
        dp[val] = min(dp[val], dp[val-v] + w)

ans = 0
for v in range(V + 1):
    if dp[v] <= W:
        ans = v

print(ans)