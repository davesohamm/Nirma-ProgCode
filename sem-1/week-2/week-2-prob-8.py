# 25MCD005 SOHAM DAVE WEEK-2 PROBLEM-8 "Beppa and SwerChat"
import sys

def solve():
    """
    Solves a single test case for the Beppa and SwerChat problem.
    """
    try:
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return

    # Create a map for O(1) lookups of positions in the 9:00 list 'a'.
    # pos_a[member_id] = index
    pos_a = {val: i for i, val in enumerate(a)}

    # Find the longest suffix of 'b' that preserves the relative order from 'a'.
    # 'k' will be the starting index of this longest valid suffix.
    k = n - 1
    while k > 0:
        # Get the current member and the one before it in the 'b' suffix.
        person_before = b[k - 1]
        person_current = b[k]

        # Check if their relative order from 'a' is maintained.
        if pos_a[person_before] < pos_a[person_current]:
            # Order is preserved, so we can extend the potential offline group.
            k -= 1
        else:
            # Order is broken. The valid suffix cannot be extended further.
            break
    
    # The number of people who must have been online is 'k'.
    # This is because b[0...k-1] are the people who are not in the
    # longest possible "offline" group.
    print(k)


def main():
    """
    Main function to handle multiple test cases.
    """
    try:
        num_test_cases = int(sys.stdin.readline())
        for _ in range(num_test_cases):
            solve()
    except (IOError, ValueError):
        pass

if __name__ == "__main__":
    main()