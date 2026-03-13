# 25MCD005 SOHAM DAVE WEEK-8 PROBLEM-3 "Books Exchange (hard version)"
import sys

def solve():
    input = sys.stdin.readline
    q = int(input())
    
    results = []
    
    for _ in range(q):
        n = int(input())
        p = [int(x) - 1 for x in input().split()]
        ans = [0] * n
        
        for i in range(n):
            if ans[i] == 0:
                current_kid = i
                cycle_length = 0
                
                while True:
                    cycle_length += 1
                    current_kid = p[current_kid]
                    if current_kid == i:
                        break
                        
                current_kid = i
                while True:
                    ans[current_kid] = cycle_length
                    current_kid = p[current_kid]
                    if current_kid == i:
                        break
                        
        results.append(" ".join(map(str, ans)))
        
    print("\n".join(results))

if __name__ == "__main__":
    solve()

