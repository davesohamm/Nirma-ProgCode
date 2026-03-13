# 25MCD005 - PROB - I
import sys
input = sys.stdin.readline

n = int(input())
p = list(map(float, input().split()))

dp = [0.0]*(n+1)
dp[0] = 1.0

for prob in p:
    for j in range(n-1, -1, -1):
        dp[j+1] += dp[j]*prob
        dp[j] *= (1-prob)

ans = 0.0
for j in range(n//2 + 1, n+1):
    ans += dp[j]

print(ans)