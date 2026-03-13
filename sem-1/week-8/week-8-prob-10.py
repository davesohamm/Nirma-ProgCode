# 25MCD005 SOHAM DAVE WEEK-8 PROBLEM-10 "Nearest Opposite Parity"
import sys
import collections

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

adj_rev = [[] for _ in range(n)]
for i in range(n):
    val = a[i]
    
    dest_left = i - val
    if 0 <= dest_left < n:
        adj_rev[dest_left].append(i)
        
    dest_right = i + val
    if 0 <= dest_right < n:
        adj_rev[dest_right].append(i)

ans = [-1] * n

dist_from_even = [-1] * n
q = collections.deque()
for i in range(n):
    if a[i] % 2 == 0:
        q.append(i)
        dist_from_even[i] = 0

while q:
    u = q.popleft()
    for v in adj_rev[u]:
        if dist_from_even[v] == -1:
            dist_from_even[v] = dist_from_even[u] + 1
            q.append(v)

dist_from_odd = [-1] * n
q = collections.deque()
for i in range(n):
    if a[i] % 2 != 0:
        q.append(i)
        dist_from_odd[i] = 0

while q:
    u = q.popleft()
    for v in adj_rev[u]:
        if dist_from_odd[v] == -1:
            dist_from_odd[v] = dist_from_odd[u] + 1
            q.append(v)

for i in range(n):
    if a[i] % 2 == 0:
        ans[i] = dist_from_odd[i]
    else:
        ans[i] = dist_from_even[i]

sys.stdout.write(" ".join(map(str, ans)) + "\n")

