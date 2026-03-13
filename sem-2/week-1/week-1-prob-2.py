# 25MCD005 SOHAM DAVE - Reverse a Substring
import sys

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        n = int(line1)
        s = sys.stdin.readline().strip()
        
        for i in range(n - 1):
            if s[i] > s[i+1]:
                print("YES")
                print(i + 1, i + 2)
                return
                
        print("NO")
    except ValueError:
        pass

if __name__ == '__main__':
    solve()