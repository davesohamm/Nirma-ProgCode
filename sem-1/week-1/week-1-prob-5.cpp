// 25MCD005 SOHAM DAVE WEEK-1 PROBLEM-5 "SUM OF THREE VALUES"
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long target;
    cin >> n >> target;
    vector<pair<long long, int>> arr(n);
    for (int i = 0; i < n; i++) {
        long long val;
        cin >> val;
        arr[i] = {val, i + 1}; // store value and original index
    }

    sort(arr.begin(), arr.end());

    for (int i = 0; i < n; i++) {
        long long a_val = arr[i].first;
        int a_idx = arr[i].second;
        int left = i + 1;
        int right = n - 1;

        while (left < right) {
            long long sum = a_val + arr[left].first + arr[right].first;
            if (sum == target) {
                cout << a_idx << " " << arr[left].second << " " << arr[right].second << "\n";
                return 0;
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
    }

    cout << "IMPOSSIBLE\n";
    return 0;
}
