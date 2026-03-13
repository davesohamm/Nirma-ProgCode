// 25MCD005 WEEK-5 PROBLEM-F Data Structures Fan
#include <iostream>
#include <vector>
#include <string>

using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    vector<int> pref(n + 1, 0);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        pref[i + 1] = pref[i] ^ a[i];
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
            int range_xor = pref[r] ^ pref[l - 1];
            x0 ^= range_xor;
            x1 ^= range_xor;
        } else {
            int g;
            cin >> g;
            cout << (g == 0 ? x0 : x1) << " ";
        }
    }
    cout << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}