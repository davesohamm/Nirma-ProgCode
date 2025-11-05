# 25MCD005 SOHAM DAVE WEEK-3 PROBLEM-9 "Divisible Numbers (easy version)"
import sys
from math import isqrt

def get_divisors(n):
    divs = set()
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return list(divs)

def solve():
    a, b, c, d = map(int, sys.stdin.readline().split())
    
    divs_a = get_divisors(a)
    divs_b = get_divisors(b)
    
    target_product = a * b
    
    for i in divs_a:
        for j in divs_b:
            d1 = i * j
            
            x = (a // d1 + 1) * d1
            
            if x > c:
                continue
            
            d2 = target_product // d1
            y = (b // d2 + 1) * d2
            
            if y <= d:
                print(x, y)
                return
                
    print(-1, -1)

def main():
    try:
        t_str = sys.stdin.readline()
        if not t_str:
            return
        t = int(t_str)
        for _ in range(t):
            solve()
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    main()