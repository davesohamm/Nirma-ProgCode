# 25MCD005 SOHAM DAVE WEEK-3 PROBLEM-10 "Magic Triples (Easy Version)"
import sys

def solve():
    try:
        n_str = sys.stdin.readline()
        if not n_str: return
        n = int(n_str)
        a = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return

    modified_indices = []
    for x in a:
        if counts[x] == 0:
            modified_indices.append(x)
        counts[x] += 1

    unique_nums = sorted(modified_indices)
    
    ans = 0
    for x in unique_nums:
        c = counts[x]
        if c >= 3:
            ans += c * (c - 1) * (c - 2)

    U = len(unique_nums)
    MAX_A = 1000000
    THRESHOLD = 800

    if U < THRESHOLD:
        for i in range(U):
            i_val = unique_nums[i]
            for j in range(i + 1, U):
                j_val = unique_nums[j]
                if j_val % i_val == 0:
                    b = j_val // i_val
                    k_val = j_val * b
                    if k_val <= MAX_A and counts[k_val] > 0:
                        ans += counts[i_val] * counts[j_val] * counts[k_val]
    else:
        max_val_in_a = unique_nums[-1]
        for i_val in unique_nums:
            b = 2
            while True:
                j_val = i_val * b
                k_val = j_val * b
                if k_val > max_val_in_a:
                    break
                
                if counts[j_val] > 0 and counts[k_val] > 0:
                    ans += counts[i_val] * counts[j_val] * counts[k_val]
                
                b += 1
    
    print(ans)

    for x in modified_indices:
        counts[x] = 0

MAX_VAL = 1000001
counts = [0] * MAX_VAL

def main():
    try:
        t_str = sys.stdin.readline()
        if t_str:
            t = int(t_str)
            for _ in range(t):
                solve()
    except (IOError, ValueError):
        pass

if __name__ == "__main__":
    main()