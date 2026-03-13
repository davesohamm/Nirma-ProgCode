# 25MCD005 SOHAM DAVE WEEK-5 PROBLEM-7 "Finding Periods"
import sys
s = sys.stdin.readline().strip()
n = len(s)
z = [0] * n
l = r = 0
for i in range(1, n):
    if i <= r:
        z[i] = min(r - i + 1, z[i - l])
    while i + z[i] < n and s[z[i]] == s[i + z[i]]:
        z[i] += 1
    if i + z[i] - 1 > r:
        l = i
        r = i + z[i] - 1

res = []
for p in range(1, n):
    if z[p] >= n - p:
        res.append(p)
res.append(n)

sys.stdout.write(" ".join(map(str, res)))
