#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

bool check(int n, ll k, const vector<int>& a, ll h) {
    for (int i = 0; i < n; i++) {
        ll current_cost = 0;
        ll needed = h;
        bool possible = false;
        
        for (int j = i; j < n; j++) {
            if (a[j] >= needed) {
                possible = true;
                break;
            }
            if (j == n - 1) break;
            current_cost += (needed - a[j]);
            needed--;
            
            if (current_cost > k) break;
        }
        if (possible && current_cost <= k) return true;
    }
    return false;
}

void solve() {
    int n;
    ll k;
    if (!(cin >> n >> k)) return;
    
    vector<int> a(n);
    int max_val = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        max_val = max(max_val, a[i]);
    }

    ll low = max_val, high = max_val + k, ans = max_val;
    while (low <= high) {
        ll mid = low + (high - low) / 2;
        if (check(n, k, a, mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
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