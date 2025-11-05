# 25MCD005 SOHAM DAVE WEEK-4 PROBLEM-1 "Minimum Absolute Difference in an Array"
def minimumAbsoluteDifference(arr):
    # Step 1: Sort the array
    arr.sort()
    
    # Step 2: Initialize the minimum difference with a large value
    min_diff = float('inf')
    
    # Step 3: Compare adjacent elements only
    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i - 1])
        if diff < min_diff:
            min_diff = diff
    
    # Step 4: Return the minimum difference found
    return min_diff


# Driver code for testing
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().split()))
    result = minimumAbsoluteDifference(arr)
    print(result)
