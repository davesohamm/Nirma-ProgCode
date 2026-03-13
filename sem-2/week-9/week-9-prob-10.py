# 25MCD005 - PROB - J
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    N = int(input_data[0])
    a = [int(x) for x in input_data[1:]]
    
    c1 = a.count(1)
    c2 = a.count(2)
    c3 = a.count(3)
    
    dp = [[0.0] * (N + 2) for _ in range(N + 2)]
    
    for i in range(c3 + 1):
        
        next_dp = [[0.0] * (N + 2) for _ in range(N + 2)]
        
        for j in range(N + 1 - i):
            
            for k in range(N + 1 - i - j):
                if i == 0 and j == 0 and k == 0:
                    continue
                    
                tot = k + j + i
                val = N / tot
                
                if k > 0:
                    val += (k / tot) * next_dp[j][k - 1]
                
                if j > 0:
                    val += (j / tot) * next_dp[j - 1][k + 1]
                
                if i > 0:
                    val += (i / tot) * dp[j + 1][k]
                    
                next_dp[j][k] = val
                
        dp = next_dp
        
    print(f"{dp[c2][c1]:.15f}")

if __name__ == '__main__':
    solve()