# 25MCD005 SOHAM DAVE WEEK-4 PROBLEM-7 "Two Substrings"
s = input()

ab_first = s.find("AB")
ba_after_ab = -1
if ab_first != -1:
    ba_after_ab = s.find("BA", ab_first + 2)

ba_first = s.find("BA")
ab_after_ba = -1
if ba_first != -1:
    ab_after_ba = s.find("AB", ba_first + 2)

if (ba_after_ab != -1) or (ab_after_ba != -1):
    print("YES")
else:
    print("NO")
