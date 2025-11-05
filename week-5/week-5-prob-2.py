# 25MCD005 SOHAM DAVE WEEK-5 PROBLEM-2 "Petya and Strings"
import sys
a = sys.stdin.readline().strip().lower()
b = sys.stdin.readline().strip().lower()
if a < b:
    sys.stdout.write("-1")
elif a > b:
    sys.stdout.write("1")
else:
    sys.stdout.write("0")
