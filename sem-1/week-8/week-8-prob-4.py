# 25MCD005 SOHAM DAVE WEEK-8 PROBLEM-4 "Kefa and Park"
import sys
import collections

def solve():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    adj = collections.defaultdict(list)
    for _ in range(n - 1):
        x, y = map(int, sys.stdin.readline().split())
        adj[x].append(y)
        adj[y].append(x)
        
    queue = collections.deque([(1, 0, 0)]) 
    safe_restaurants_count = 0
    
    if n == 1:
        if a[0] <= m:
            print(1)
        else:
            print(0)
        return

    while queue:
        u, p, cons_cats = queue.popleft()
        
        if a[u-1] == 1:
            new_cons_cats = cons_cats + 1
        else:
            new_cons_cats = 0
            
        if new_cons_cats > m:
            continue
            
        is_leaf = True
        for v in adj[u]:
            if v != p:
                is_leaf = False
                queue.append((v, u, new_cons_cats))
                
        if is_leaf:
            safe_restaurants_count += 1
            
    print(safe_restaurants_count)

solve()

