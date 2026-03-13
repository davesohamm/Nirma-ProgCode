# 25MCD005 SOHAM DAVE - Sea and Islands
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    k = int(input_data[1])
    
    max_possible = (n * n + 1) // 2
    
    if k > max_possible:
        print("NO")
        return
        
    print("YES")
    
    islands_placed = 0
    for i in range(n):
        row = []
        for j in range(n):
            if (i + j) % 2 == 0 and islands_placed < k:
                row.append('L')
                islands_placed += 1
            else:
                row.append('S')
        print("".join(row))

if __name__ == '__main__':
    solve()