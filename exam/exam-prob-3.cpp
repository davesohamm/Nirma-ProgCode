// 25MCD005 EXAM-PROBLEM-3
/*
Problem: Factory Machines

A factory has n machines that can be used to produce products. Your goal is to make a total of t products.

For each machine, you know the number of seconds it takes to produce one product. All machines
can work simultaneously, and you are free to schedule them however you want.

Your task is to determine the minimum time required to produce t products in total.

Input:
- The first line contains two integers n and t:
    n = number of machines
    t = number of products required

- The second line contains n integers k1, k2, ..., kn:
    ki = time in seconds needed for machine i to make one product

Output:
- Print one integer: the minimum time required to make t products.

Constraints:
1 ≤ n ≤ 2 * 10^5
1 ≤ t ≤ 10^9
1 ≤ ki ≤ 10^9

Example:
Input:
    3 7
    3 2 5
Output:
    8

Explanation:
Machine 1 makes 2 products, machine 2 makes 4 products,
and machine 3 makes 1 product in 8 seconds, for a total of 7 products.
*/


#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

bool check(long long time, const vector<long long>& k, long long t) {
    long long products_made = 0;
    for (long long rate : k) {
        products_made += time / rate;
        if (products_made >= t) return true;
    }
    return products_made >= t;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long n, t;
    if (!(cin >> n >> t)) return 0;

    vector<long long> k(n);
    long long min_k = LLONG_MAX;
    for (int i = 0; i < n; ++i) {
        cin >> k[i];
        if (k[i] < min_k) {
            min_k = k[i];
        }
    }

    long long left = 0, right = min_k * t + 1;
    long long ans = right;

    while (left <= right) {
        long long mid = left + (right - left) / 2;
        if (check(mid, k, t)) {
            ans = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    cout << ans << endl;

    return 0;
}