// 25MCD005 EXAM-PROBLEM-5
/*
Problem: Longest Increasing Subsequence (LIS)

You are given an array of n integers. Your task is to determine the length of the
longest increasing subsequence in the array, i.e., the longest subsequence where
every element is strictly larger than the previous one.

A subsequence is a sequence that can be derived from the array by deleting some
elements without changing the order of the remaining elements.

Input:
- The first line contains an integer n: the size of the array.
- The second line contains n integers x1, x2, ..., xn: the elements of the array.

Output:
- Print one integer: the length of the longest increasing subsequence.

Constraints:
1 ≤ n ≤ 2 * 10^5
1 ≤ xi ≤ 10^9

Example:
Input:
    8
    7 3 5 3 6 2 9 8
Output:
    4

Explanation:
One possible longest increasing subsequence is {3, 5, 6, 9}.
*/


#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    int n;
    if (!(cin >> n)) return 1;
    
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }

    if (n == 0) {
        cout << 0 << endl;
        return 0;
    }

    vector<int> tail;
    for (int num : nums) {
        auto it = lower_bound(tail.begin(), tail.end(), num);
        if (it == tail.end()) {
            tail.push_back(num);
        } else {
            *it = num;
        }
    }
    cout << tail.size() << endl;

    return 0;
}


