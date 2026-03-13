# 25MCD005 SOHAM DAVE - Expansion coefficient of the array
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = list(map(int, input_data[1:]))
    
    ans = 10**18
    
    for i in range(n):
        dist = max(i, n - 1 - i)
        ans = min(ans, a[i] // dist)
        
    print(ans)

if __name__ == "__main__":
    solve()