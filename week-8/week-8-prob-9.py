# 25MCD005 SOHAM DAVE WEEK-8 PROBLEM-9 "Fox And Names"
import sys
from collections import deque
import string

def solve():
    try:
        n_str = sys.stdin.readline()
        if not n_str:
            return 
        n = int(n_str.strip())
        names = [sys.stdin.readline().strip() for _ in range(n)]

        adj = {c: set() for c in string.ascii_lowercase}
        in_degree = {c: 0 for c in string.ascii_lowercase}
        
        impossible = False

        for i in range(n - 1):
            s1, s2 = names[i], names[i+1]
            l1, l2 = len(s1), len(s2)
            j = 0
            found_diff = False
            while j < l1 and j < l2:
                if s1[j] != s2[j]:
                    if s2[j] not in adj[s1[j]]:
                        adj[s1[j]].add(s2[j])
                        in_degree[s2[j]] += 1
                    found_diff = True
                    break
                j += 1
            
            if not found_diff and l1 > l2:
                impossible = True
                break
        
        if impossible:
            print("Impossible")
            return

        queue = deque([c for c in string.ascii_lowercase if in_degree[c] == 0])
        result = []
        
        while queue:
            u = queue.popleft()
            result.append(u)
            
            for v in sorted(list(adj[u])):
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        if len(result) == 26:
            print("".join(result))
        else:
            print("Impossible")

    except EOFError:
        pass
    except Exception as e:
        pass

if __name__ == "__main__":
    solve()

