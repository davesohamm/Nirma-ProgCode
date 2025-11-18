# 25MCD005 SOHAM DAVE WEEK-9 PROBLEM-5 "Knapsack 2"
import sys

def solve():
    n, w_cap = map(int, sys.stdin.readline().split())
    items = []
    for _ in range(n):
        items.append(list(map(int, sys.stdin.readline().split())))

    max_val = n * 1000
    dp = [float('inf')] * (max_val + 1)
    dp[0] = 0

    for w, v in items:
        for val in range(max_val, v - 1, -1):
            if dp[val - v] != float('inf'):
                dp[val] = min(dp[val], dp[val - v] + w)

    ans = 0
    for val in range(max_val, -1, -1):
        if dp[val] <= w_cap:
            ans = val
            break
            
    print(ans)

if __name__ == "__main__":
    solve()