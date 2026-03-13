# 25MCD005 SOHAM DAVE WEEK-8 PROBLEM-5 "Course Schedule"
import sys
from collections import deque

def solve():
    try:
        n, m = map(int, sys.stdin.readline().split())
        
        adj = [[] for _ in range(n + 1)]
        in_degree = [0] * (n + 1)
        
        for _ in range(m):
            a, b = map(int, sys.stdin.readline().split())
            adj[a].append(b)
            in_degree[b] += 1
            
        queue = deque()
        for i in range(1, n + 1):
            if in_degree[i] == 0:
                queue.append(i)
                
        result = []
        
        while queue:
            u = queue.popleft()
            result.append(u)
            
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        if len(result) == n:
            print(*(result))
        else:
            print("IMPOSSIBLE")

    except EOFError:
        pass
    except Exception as e:
        pass

if __name__ == "__main__":
    solve()
