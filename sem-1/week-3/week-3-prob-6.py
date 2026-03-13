# 25MCD005 SOHAM DAVE WEEK-3 PROBLEM-6 "Buying Shovels"
import math
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k >= n:
        print(1)
        continue
    ans = n
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i <= k:
                ans = min(ans, n // i)
            if n // i <= k:
                ans = min(ans, i)
        i += 1
    print(ans)
