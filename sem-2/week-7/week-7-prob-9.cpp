#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void solve() {
    string s;
    cin >> s;
    
    int sz = 0;
    int sorted_until = 0;
    int min_unsorted = 1e9; // Initialize to infinity
    
    for (char c : s) {
        if (c == '+') {
            sz++;
            if (sz == 1) sorted_until = 1;
        } else if (c == '-') {
            sz--;
            if (sorted_until > sz) sorted_until = sz;
            if (min_unsorted > sz) min_unsorted = 1e9;
        } else if (c == '1') {
            if (min_unsorted <= sz) {
                cout << "NO\n";
                return;
            }
            sorted_until = sz;
        } else if (c == '0') {
            if (sz < 2 || sorted_until == sz) {
                cout << "NO\n";
                return;
            }
            if (min_unsorted > sz) {
                min_unsorted = sz;
            }
        }
    }
    cout << "YES\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}