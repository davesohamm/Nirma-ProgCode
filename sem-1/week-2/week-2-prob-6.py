# 25MCD005 SOHAM DAVE WEEK-2 PROBLEM-6 "Min-Max Array Transformation"
import sys

def solve():
    """
    Solves a single test case for the Min-Max Array Transformation problem.
    """
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    # --- Calculate d_min for each element ---
    # To minimize d_i = b_j - a_i, we need the smallest b_j >= a_i.
    # We use a two-pointer approach. j moves forward to find the
    # first b[j] that is >= a[i].
    d_min = []
    j = 0
    for i in range(n):
        # Find the first b[j] that's large enough for a[i]
        while b[j] < a[i]:
            j += 1
        d_min.append(b[j] - a[i])

    # --- Calculate d_max for each element ---
    # To maximize d_i = b_j - a_i, we want the largest possible b_j.
    # We iterate from the end. j is the index of the max b value available.
    d_max = [0] * n
    j = n - 1
    for i in range(n - 1, -1, -1):
        # The maximum possible value for a[i] + d[i] is b[j].
        d_max[i] = b[j] - a[i]
        
        # If a[i] > b[i-1], it creates a partition.
        # {a_0, ..., a_{i-1}} must map to {b_0, ..., b_{i-1}}.
        # Thus, for a_{i-1} and all before it, the max b they can map to is b_{i-1}.
        # This happens when the current mapping boundary `j` is at `i`.
        if i > 0 and a[i] > b[i-1]:
             # If a[i] > b[i-1], this means {a[i], ..., a[n-1]} must map to
             # {b[i], ..., b[n-1]}.
             # Consequently, {a[0], ..., a[i-1]} must map to {b[0], ..., b[i-1]}.
             # This means for a[i-1], the largest element it can map to is b[i-1].
             # We update our boundary pointer `j` for the next iterations.
             j = i - 1


    print(*d_min)
    print(*d_max)


def main():
    """
    Main function to handle multiple test cases.
    """
    try:
        num_test_cases = int(sys.stdin.readline())
        for _ in range(num_test_cases):
            solve()
    except (IOError, ValueError):
        # Handle cases with no input or empty lines
        pass

if __name__ == "__main__":
    main()
