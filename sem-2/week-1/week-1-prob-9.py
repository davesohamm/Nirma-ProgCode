# 25MCD005 SOHAM DAVE - Periodic integer number
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    L = int(input_data[0])
    A = input_data[1]
    N = len(A)
    
    rem = N % L
    if rem == 0:
        target_len = N
    else:
        target_len = N + (L - rem)
        
    if target_len > N:
        pattern = '1' + '0' * (L - 1)
        repeats = target_len // L
        sys.stdout.write(pattern * repeats + '\n')
        return

    prefix = A[:L]
    repeats = N // L
    candidate = prefix * repeats
    
    if candidate > A:
        sys.stdout.write(candidate + '\n')
    else:
        p_list = list(prefix)
        i = L - 1
        while i >= 0:
            if p_list[i] == '9':
                p_list[i] = '0'
                i -= 1
            else:
                p_list[i] = chr(ord(p_list[i]) + 1)
                break
        
        if i < 0:
            new_total_len = N + L
            pattern = '1' + '0' * (L - 1)
            sys.stdout.write(pattern * (new_total_len // L) + '\n')
        else:
            new_prefix = "".join(p_list)
            sys.stdout.write(new_prefix * repeats + '\n')

if __name__ == '__main__':
    solve()