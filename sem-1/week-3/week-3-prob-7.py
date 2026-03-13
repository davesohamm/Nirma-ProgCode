# 25MCD005 SOHAM DAVE WEEK-3 PROBLEM-7 "Number into Sequence"
import math
t = int(input())
for _ in range(t):
    n = int(input())
    x = n
    best = 1
    temp = 2
    while temp * temp <= x:
        cnt = 0
        while x % temp == 0:
            x //= temp
            cnt += 1
        if cnt > best:
            best = cnt
            prime = temp
        temp += 1
    if x > 1 and best == 1:
        print(1)
        print(n)
        continue
    seq = []
    val = n
    for _ in range(best - 1):
        seq.append(prime)
        val //= prime
    seq.append(val)
    print(len(seq))
    print(*seq)
