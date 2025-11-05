# 25MCD005 SOHAM DAVE WEEK-5 PROBLEM-8 "Palindrome Pairs"
import sys

def solve():
    try:
        n_line = sys.stdin.readline()
        if not n_line:
            print(0)
            return
            
        n = int(n_line.strip())
        if n == 0:
            print(0)
            return

        freq = {}
        for _ in range(n):
            s = sys.stdin.readline().strip()
            if not s:
                continue
            
            mask = 0
            for char in s:
                bit_pos = ord(char) - ord('a')
                mask ^= (1 << bit_pos)
            freq[mask] = freq.get(mask, 0) + 1

        total_pairs = 0
        masks = list(freq.keys())
        
        for m in masks:
            count = freq[m]
            total_pairs += (count * (count - 1)) // 2

            for l in range(26):
                m_prime = m ^ (1 << l)
                if m_prime in freq and m < m_prime:
                     total_pairs += count * freq[m_prime]

        print(total_pairs)

    except EOFError:
        pass
    except Exception:
        pass

solve()


