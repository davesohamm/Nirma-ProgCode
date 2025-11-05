// 25MCD005 SOHAM DAVE WEEK-1 PROBLEM-6 "ARRAY DIVISION"
#include <bits/stdc++.h>
using namespace std;

bool canDivide(const vector<long long>& arr, int m, long long maxSum) {
    int cnt = 1;
    long long curr = 0;
    for (auto x : arr) {
        if (curr + x > maxSum) {
            cnt++;
            curr = x;
        } else {
            curr += x;
        }
    }
    return cnt <= m;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    vector<long long> arr(n);
    long long low = 0, high = 0;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        low = max(low, arr[i]);
        high += arr[i];
    }

    long long ans = high;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (canDivide(arr, k, mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
