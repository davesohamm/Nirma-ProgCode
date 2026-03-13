# 25MCD005 SOHAM DAVE - Team Formation
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    q = int(input_data[ptr])
    ptr += 1
    
    results = []
    for _ in range(q):
        n = int(input_data[ptr])
        s = input_data[ptr + 1]
        t = input_data[ptr + 2]
        ptr += 3
        
        c11, c10, c01, c00 = 0, 0, 0, 0
        
        for i in range(n):
            if s[i] == '1' and t[i] == '1':
                c11 += 1
            elif s[i] == '1' and t[i] == '0':
                c10 += 1
            elif s[i] == '0' and t[i] == '1':
                c01 += 1
            else:
                c00 += 1
        
        teams = 0
        
        pair_specialized = min(c10, c01)
        teams += pair_specialized
        c10 -= pair_specialized
        c01 -= pair_specialized
        
        remaining_individuals = c10 + c01 + c00
        
        while c11 > 0:
            if remaining_individuals > 0:
                teams += 1
                c11 -= 1
                remaining_individuals -= 1
            elif c11 >= 2:
                teams += 1
                c11 -= 2
            else:
                break
                
        results.append(str(teams))
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()