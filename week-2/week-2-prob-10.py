# 25MCD005 SOHAM DAVE WEEK-2 PROBLEM-10 "Moscow Gorillas"
import sys

def count_triangular(k):
    """Calculates the k-th triangular number: 1 + 2 + ... + k."""
    if k <= 0:
        return 0
    return k * (k + 1) // 2

def count_rect(x1, y1, x2, y2):
    """
    Counts pairs (l, r) with x1 <= l <= y1, x2 <= r <= y2, and l <= r.
    This is an O(1) calculation.
    """
    if x1 > y1 or x2 > y2:
        return 0

    if y1 < x2:
        # l is always less than r, forms a simple rectangle.
        return (y1 - x1 + 1) * (y2 - x2 + 1)
    else:
        # The region is more complex and needs to be split.
        total = 0
        # Part 1: l < x2. Here, l is always < r.
        if x1 < x2:
            len_l1 = x2 - x1
            len_r1 = y2 - x2 + 1
            total += len_l1 * len_r1
        
        # Part 2: l >= x2. This forms a triangular/trapezoidal region.
        # We need to sum (y2 - l + 1) for l from max(x1, x2) to y1.
        start_l = max(x1, x2)
        if start_l <= y1:
            num_terms = y1 - start_l + 1
            first_term = y2 - start_l + 1
            last_term = y2 - y1 + 1
            total += num_terms * (first_term + last_term) // 2
        return total

def solve():
    """
    Solves the Moscow Gorillas problem in O(N) time.
    """
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    q = list(map(int, sys.stdin.readline().split()))

    pos_p = [0] * (n + 1)
    pos_q = [0] * (n + 1)
    for i in range(n):
        pos_p[p[i]] = i
        pos_q[q[i]] = i

    total_count = 0

    # --- Case 1: MEX = 1 ---
    # The segment must not contain the number 1 in either permutation.
    p1, q1 = pos_p[1], pos_q[1]
    x, y = min(p1, q1), max(p1, q1)
    # Segments entirely to the left of x
    total_count += count_triangular(x)
    # Segments entirely between x and y
    total_count += count_triangular(y - x - 1)
    # Segments entirely to the right of y
    total_count += count_triangular(n - 1 - y)

    # --- Case m > 1 ---
    min_p_so_far, max_p_so_far = pos_p[1], pos_p[1]
    min_q_so_far, max_q_so_far = pos_q[1], pos_q[1]
    
    # Loop for MEX from 2 to n
    for m in range(2, n + 1):
        L = min(min_p_so_far, min_q_so_far)
        R = max(max_p_so_far, max_q_so_far)
        
        # BUG FIX 1: The length of the span [L,R] must be >= m-1 to contain {1..m-1}
        if R - L + 1 >= m - 1:
            P = pos_p[m]
            Q = pos_q[m]

            # Count all segments containing {1..m-1}
            count_base = count_rect(0, L, R, n - 1)

            # Use inclusion-exclusion to subtract segments that also contain m
            invalid_p = count_rect(0, min(L, P), max(R, P), n - 1)
            invalid_q = count_rect(0, min(L, Q), max(R, Q), n - 1)
            invalid_pq = count_rect(0, min(L, P, Q), max(R, P, Q), n - 1)
            
            count_m = count_base - (invalid_p + invalid_q - invalid_pq)
            total_count += count_m

        # Update bounds for the next iteration to include the number m
        min_p_so_far = min(min_p_so_far, pos_p[m])
        max_p_so_far = max(max_p_so_far, pos_p[m])
        min_q_so_far = min(min_q_so_far, pos_q[m])
        max_q_so_far = max(max_q_so_far, pos_q[m])

    # BUG FIX 2: Manually add the case for MEX = n + 1
    # Only the full array segment [1..n] can have MEX n+1, and it always does.
    total_count += 1

    print(total_count)

solve()


