# 25MCD005 SOHAM DAVE WEEK-10 PROBLEM-9 "AND, OR and square sum"
import sys

n = int(sys.stdin.readline())

if n > 0:
    a = list(map(int, sys.stdin.readline().split()))
else:
    a = []
    print(0)
    sys.exit()

counts = [0] * 20

for num in a:
    for k in range(20):
        if (num >> k) & 1:
            counts[k] += 1

total_sum_sq = 0
for i in range(n):
    current_num = 0
    for k in range(20):
        if counts[k] > i:
            current_num += (1 << k)
    
    if current_num == 0:
        break
        
    total_sum_sq += current_num * current_num

print(total_sum_sq)