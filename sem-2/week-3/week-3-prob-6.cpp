// 25MCD005 PROBLEM F - SHUFFLE
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void solve() {
    long long n, x, m;
    if (!(cin >> n >> x >> m)) return;

    long long current_l = x;
    long long current_r = x;

    for (int i = 0; i < m; ++i) {
        long long l, r;
        cin >> l >> r;
        if (max(current_l, l) <= min(current_r, r)) {
            current_l = min(current_l, l);
            current_r = max(current_r, r);
        }
    }

    cout << (current_r - current_l + 1) << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}