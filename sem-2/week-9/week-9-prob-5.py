# 25MCD005 - PROB - E
import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

n, m = len(s), len(t)

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

i, j = n, m
ans = []

while i > 0 and j > 0:
    if s[i-1] == t[j-1]:
        ans.append(s[i-1])
        i -= 1
        j -= 1
    elif dp[i-1][j] >= dp[i][j-1]:
        i -= 1
    else:
        j -= 1

print("".join(reversed(ans)))