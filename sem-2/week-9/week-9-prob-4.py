# 25MCD005 - PROB - D
import sys
input = sys.stdin.readline

n, W = map(int, input().split())

dp = [0] * (W + 1)

for _ in range(n):
    w, v = map(int, input().split())
    
    for weight in range(W, w-1, -1):
        dp[weight] = max(dp[weight], dp[weight-w] + v)

print(max(dp))