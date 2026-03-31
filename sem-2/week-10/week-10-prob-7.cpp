#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

void solve() {
    int n;
    ll k;
    if (!(cin >> n >> k)) return;
    vector<ll> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    if (k >= 3) {
        cout << 0 << "\n";
        return;
    }

    sort(a.begin(), a.end());

    ll min_val = a[0];
    for (int i = 0; i < n - 1; i++) {
        min_val = min(min_val, a[i + 1] - a[i]);
    }

    if (k == 1) {
        cout << min_val << "\n";
        return;
    }

    ll ans = min_val;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            ll diff = a[j] - a[i];
            auto it = lower_bound(a.begin(), a.end(), diff);
            if (it != a.end()) {
                ans = min(ans, *it - diff);
            }
            if (it != a.begin()) {
                ans = min(ans, diff - *prev(it));
            }
        }
    }
    cout << ans << "\n";
}

int main() {
    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        solve();
    }
    return 0;
}