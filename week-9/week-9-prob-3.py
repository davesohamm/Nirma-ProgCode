# 25MCD005 SOHAM DAVE WEEK-9 PROBLEM-3 "Frog 2"
import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    h = list(map(int, sys.stdin.readline().split()))
    
    dp = [float('inf')] * n
    dp[0] = 0
    
    for i in range(1, n):
        for j in range(max(0, i - k), i):
            cost = dp[j] + abs(h[i] - h[j])
            dp[i] = min(dp[i], cost)
            
    print(dp[n-1])

if __name__ == "__main__":
    solve()