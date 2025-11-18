# 25MCD005 SOHAM DAVE WEEK-10 PROBLEM-10 "Compress Words"
import sys

def compute_pi(s):
    n = len(s)
    pi = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

def solve():
    try:
        n_line = sys.stdin.readline()
        if not n_line:
            return
        
        n = int(n_line.strip())
        if n == 0:
            print("")
            return
        
        words_line = sys.stdin.readline()
        if not words_line:
            print("")
            return

        words = words_line.split()
        
        if not words:
             print("")
             return
        
        result = words[0]
        
        for i in range(1, n):
            if i >= len(words):
                break
            
            b = words[i]
            len_b = len(b)
            if len_b == 0:
                continue
                
            a_suffix = result[max(0, len(result) - len_b):]
            
            s = b + "#" + a_suffix
            
            pi = compute_pi(s)
            
            overlap = 0
            if pi:
                overlap = pi[-1]
            
            result += b[overlap:]
            
        print(result)

    except EOFError:
        pass
    except Exception:
        pass

solve()