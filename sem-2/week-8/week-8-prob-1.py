# 25MCD005 - PROB - A - Destroying Bridges

def destroyingBridges(n, k):
    if k >= n - 1:
        return 1
    return n

x = input()

for num in range(int(x)):
    y = input()
    nk = y.split()
    n = int(nk[0])
    k = int(nk[1])

    print(destroyingBridges(n, k))