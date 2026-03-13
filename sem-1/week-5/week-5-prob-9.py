# 25MCD005 SOHAM DAVE WEEK-5 PROBLEM-9 "Longest Palindrome"
def longest_palindrome(s):
    # Transform the string: add separators to handle even-length palindromes
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n
    center = right = 0
    max_len = 0
    max_center = 0

    for i in range(n):
        mirror = 2 * center - i
        if i < right:
            p[i] = min(right - i, p[mirror])

        # Expand around center i
        while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and t[i - p[i] - 1] == t[i + p[i] + 1]:
            p[i] += 1

        # Update center and right boundary
        if i + p[i] > right:
            center = i
            right = i + p[i]

        # Track the longest palindrome
        if p[i] > max_len:
            max_len = p[i]
            max_center = i

    # Extract and return result (remove '#')
    start = (max_center - max_len) // 2
    return s[start:start + max_len]


# Input / Output handling
s = input().strip()
print(longest_palindrome(s))
