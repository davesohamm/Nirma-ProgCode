# 25MCD005 SOHAM DAVE WEEK-1 PROBLEM-8 "CUTTING OUT"
import sys
from collections import Counter

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        n, k = map(int, line1.split())
    except EOFError:
        return
    except ValueError:
        return
        
    try:
        s = list(map(int, sys.stdin.readline().split()))
    except EOFError:
        s = []
    except ValueError:
        s = []

    if n == 0 or k == 0 or len(s) != n:
        return

    s_counts = Counter(s)

    def get_max_length_for_cuts(C):
        if C == 0:
            return n 
        
        total_possible_length = 0
        for count in s_counts.values():
            total_possible_length += count // C
            
        return total_possible_length

    low = 1
    high = n + 2 
    best_C = 0

    while low < high:
        mid = low + (high - low) // 2
        
        if get_max_length_for_cuts(mid) >= k:
            best_C = mid
            low = mid + 1 
        else:
            high = mid 

    C_max = best_C
    
    t = []
    elements_added = 0
    
    for element, count in sorted(s_counts.items()):
        
        max_t_count = count // C_max
        
        take_count = min(max_t_count, k - elements_added)
        
        t.extend([element] * take_count)
        elements_added += take_count
        
        if elements_added == k:
            break

    print(*(t))

if __name__ == "__main__":
    solve()
