# 25MCD005 SOHAM DAVE WEEK-2 PROBLEM-7 "Uniqueness"
import sys

def solve():
    """
    Finds the minimum size of a subsegment to remove to make all remaining
    elements distinct.
    """
    try:
        n = int(sys.stdin.readline())
        if n == 0:
            print(0)
            return
        a = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        # Handle empty input
        print(0)
        return

    # --- Step 1: Find the longest unique suffix from the right ---
    # `r` will be the starting index of this suffix.
    # `s` will store the unique elements of the suffix.
    s = set()
    r = n
    for i in range(n - 1, -1, -1):
        if a[i] in s:
            break
        s.add(a[i])
        r = i

    # --- Step 2: Initialize the answer ---
    # Our first potential answer is to remove the prefix a[0...r-1].
    # The length of this removed segment is r.
    min_len = r

    # --- Step 3: Iterate from the left, expanding the prefix ---
    # `l` represents the end of the prefix a[0...l-1].
    # For each element a[l] added to the prefix, we may need to shrink
    # the suffix from the left (by incrementing r) to maintain uniqueness.
    prefix_elements = set()
    for l in range(n):
        # If the current element creates a duplicate in the prefix, we can't extend it further.
        if a[l] in prefix_elements:
            break
        prefix_elements.add(a[l])

        # Shrink the suffix from the left as long as the new prefix element a[l]
        # is present in the suffix set `s`.
        while r < n and a[l] in s:
            s.remove(a[r])
            r += 1

        # Calculate the length of the removed segment a[l+1...r-1]
        # and update the minimum length.
        # The length is r - (l + 1).
        min_len = min(min_len, r - (l + 1))

    print(min_len)

solve()
