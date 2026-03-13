// 25MCD005 WEEK-4 PROBLEM-H Plus and Multiply
#include <iostream>

using namespace std;

void solve() {
    long long n, a, b;
    cin >> n >> a >> b;
    if (a == 1) {
        if ((n - 1) % b == 0) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
        return;
    }
    long long curr = 1;
    bool found = false;
    while (curr <= n) {
        if ((n - curr) % b == 0) {
            found = true;
            break;
        }
        curr *= a;
    }
    if (found) cout << "Yes" << endl;
    else cout << "No" << endl;
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