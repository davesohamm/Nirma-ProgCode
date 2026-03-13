# 25MCD005 SOHAM DAVE WEEK-8 PROBLEM-8 "Building Teams"
import sys
import collections

n, m = map(int, sys.stdin.readline().split())
adj = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

teams = [0] * (n + 1)
is_possible = True
queue = collections.deque()

for i in range(1, n + 1):
    if teams[i] == 0:
        teams[i] = 1
        queue.append(i)
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if teams[v] == 0:
                    teams[v] = 3 - teams[u]
                    queue.append(v)
                elif teams[v] == teams[u]:
                    is_possible = False
                    break
            if not is_possible:
                break
    if not is_possible:
        break

if is_possible:
    print(*(teams[1:]))
else:
    print("IMPOSSIBLE")

