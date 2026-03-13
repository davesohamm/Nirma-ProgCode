# 25MCD005 SOHAM DAVE WEEK-2 PROBLEM-2 "Black and White Stripe"
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    
    # Count white cells in the first window of size k
    white_count = s[:k].count('W')
    min_recolor = white_count  # Best so far
    
    # Slide the window across the string
    for i in range(k, n):
        # Remove the leftmost character if it's 'W'
        if s[i - k] == 'W':
            white_count -= 1
        # Add the new character if it's 'W'
        if s[i] == 'W':
            white_count += 1
        
        min_recolor = min(min_recolor, white_count)
    
    print(min_recolor)
