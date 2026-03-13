# 25MCD005 - PROB - B - Metro

N, S = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

flag = False

for i in range(1, N):
    if a[i] == 1 and i == S - 1:
        flag = True
    elif a[i] == 1 and i > S - 1 and b[i] == 1 and b[S - 1] == 1:
        flag = True

if a[0] == 0:
    flag = False

if flag:
    print("YES")
else:
    print("NO")