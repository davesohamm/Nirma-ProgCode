# 25MCD005 SOHAM DAVE - Array Sharpening
import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []

    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = list(map(int, input[ptr : ptr + n]))
        ptr += n

        prefix_end = -1
        for i in range(n):
            if a[i] >= i:
                prefix_end = i
            else:
                break
        
        suffix_start = n
        for i in range(n - 1, -1, -1):
            if a[i] >= (n - 1 - i):
                suffix_start = i
            else:
                break
        
        if prefix_end >= suffix_start:
            results.append("Yes")
        else:
            results.append("No")

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()