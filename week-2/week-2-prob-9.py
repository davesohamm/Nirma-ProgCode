# 25MCD005 SOHAM DAVE WEEK-2 PROBLEM-9 "Longest k-Good Segment"
import sys

def solve():
    """
    Finds the longest k-good segment using a sliding window approach.
    """
    try:
        # Fast I/O for large inputs
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        # Handle empty input at the end of test files
        return

    # 'left' pointer for the sliding window
    left = 0
    # Dictionary to store frequencies of elements in the current window
    counts = {}
    
    # Variables to store the result (1-based indices)
    max_len = 0
    ans_l, ans_r = 1, 1

    # 'right' pointer expands the window to the right
    for right in range(n):
        # Add the new element to the window and update its count
        num = a[right]
        counts[num] = counts.get(num, 0) + 1

        # If the window is no longer k-good, shrink it from the left
        while len(counts) > k:
            left_num = a[left]
            counts[left_num] -= 1
            # If an element's count drops to zero, remove it from our distinct count
            if counts[left_num] == 0:
                del counts[left_num]
            left += 1

        # Check if the current valid window is the longest found so far
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
            # Store the 1-based indices of the longest segment
            ans_l = left + 1
            ans_r = right + 1
            
    print(ans_l, ans_r)

solve()