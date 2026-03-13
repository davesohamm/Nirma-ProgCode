# 25MCD005 SOHAM DAVE WEEK-2 PROBLEM-1 "Serval and Inversion Magic"
def can_be_palindrome_after_one_flip(s):
    n = len(s)
    mismatches = []
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            mismatches.append(i)
    
    if not mismatches:
        # Already a palindrome
        return True
    
    # Check if mismatches form a contiguous block
    if mismatches[-1] - mismatches[0] + 1 == len(mismatches):
        return True
    return False

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    print("Yes" if can_be_palindrome_after_one_flip(s) else "No")

