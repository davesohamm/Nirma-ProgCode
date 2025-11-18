# 25MCD005 SOHAM DAVE WEEK-10 PROBLEM-8 "AGAGA XOOORRR"
import sys
from functools import reduce

def solve():
    try:
        t_line = sys.stdin.readline()
        if not t_line:
            return
        t = int(t_line)
    except (IOError, ValueError):
        return

    results = []
    for _ in range(t):
        try:
            n_line = sys.stdin.readline()
            if not n_line:
                break
            n = int(n_line)
            
            a_line = sys.stdin.readline()
            if not a_line:
                break
            a = list(map(int, a_line.split()))
            
            if not a or len(a) != n:
                break
                
        except (IOError, ValueError):
            break

        total_xor = reduce(lambda x, y: x ^ y, a, 0)
        
        if total_xor == 0:
            results.append("YES")
            continue
        
        current_xor = 0
        partitions = 0
        
        for x in a:
            current_xor ^= x
            if current_xor == total_xor:
                partitions += 1
                current_xor = 0
        
        if current_xor == 0 and partitions >= 3:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()