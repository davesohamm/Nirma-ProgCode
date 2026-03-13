// 25MCD005 PROBLEM B - Powered Addition
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<long long> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        long long max_val = a[0];
        long long max_diff = 0;
        for (int i = 1; i < n; i++) {
            if (a[i] < max_val) {
                max_diff = max(max_diff, max_val - a[i]);
            } else {
                max_val = a[i];
            }
        }
        if (max_diff == 0) {
            cout << 0 << endl;
        } else {
            long long ans = 0;
            while ((1LL << ans) - 1 < max_diff) {
                ans++;
            }
            cout << ans << endl;
        }
    }
    return 0;
}