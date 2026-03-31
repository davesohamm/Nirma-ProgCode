#include <iostream>
#include <vector>
#include <string>
using namespace std;
void solve() {
    int n;
    if (!(cin >> n)) return;
    vector<int> a(n);
    vector<int> pre(n + 1, 0);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        pre[i + 1] = pre[i] ^ a[i];
    }
    string s;
    cin >> s;
    int x0 = 0, x1 = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '0') x0 ^= a[i];
        else x1 ^= a[i];
    }
    int q;
    cin >> q;
    while (q--) {
        int tp;
        cin >> tp;
        if (tp == 1) {
            int l, r;
            cin >> l >> r;
            int range_xor = pre[r] ^ pre[l - 1];
            x0 ^= range_xor;
            x1 ^= range_xor;
        } else {
            int g;
            cin >> g;
            if (g == 0) cout << x0 << " ";
            else cout << x1 << " ";
        }
    }
    cout << "\n";
}

int main() {
    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        solve();
    }
    return 0;
}