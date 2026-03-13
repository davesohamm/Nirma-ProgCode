// 25MCD005 SOHAM DAVE WEEK-1 PROBLEM-7 "SUBARRAY DIVISIBILITY"
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    map<long long, long long> freq;
    freq[0] = 1;
    long long prefix = 0, count = 0;

    for (int i = 0; i < n; i++) {
        prefix += arr[i];
        long long mod = ((prefix % n) + n) % n;
        count += freq[mod];
        freq[mod]++;
    }

    cout << count << "\n";
    return 0;
}
