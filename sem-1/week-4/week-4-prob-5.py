# 25MCD005 SOHAM DAVE WEEK-4 PROBLEM-5 "Max Min"
def maxMin(k, arr):
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr) - k + 1):
        diff = arr[i + k - 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff

if __name__ == "__main__":
    n = int(input().strip())
    k = int(input().strip())
    arr = [int(input().strip()) for _ in range(n)]
    print(maxMin(k, arr))
