# 25MCD005 SOHAM DAVE WEEK-1 PROBLEM-4 "K-TH NOT DIVISIBLE BY N"
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    blocks = k // (n - 1)
    offset = k % (n - 1)
    if offset == 0:
        ans = blocks * n - 1
    else:
        ans = blocks * n + offset
    print(ans)
