// 25MCD005 WEEK-4 PROBLEM-G k-LCM (easy version)
#include <iostream>

using namespace std;

void solve() {
    int n, k;
    cin >> n >> k;
    if (n % 2 != 0) {
        cout << 1 << " " << n / 2 << " " << n / 2 << endl;
    } else {
        if (n % 4 == 0) {
            cout << n / 2 << " " << n / 4 << " " << n / 4 << endl;
        } else {
            cout << 2 << " " << n / 2 - 1 << " " << n / 2 - 1 << endl;
        }
    }
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