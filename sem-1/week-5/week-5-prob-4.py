# 25MCD005 SOHAM DAVE WEEK-5 PROBLEM-4 "DString LCM"
import math
for _ in range(int(input())):
    s = input()
    t = input()
    l = math.lcm(len(s), len(t))
    if s * (l // len(s)) == t * (l // len(t)):
        print(s * (l // len(s)))
    else:
        print(-1)
