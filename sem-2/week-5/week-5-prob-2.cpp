// 25MCD005 WEEK-5 PROBLEM-B Mocha and Math
#include <iostream>
#include <vector>

using namespace std;

void solve() {
    int n;
    cin >> n;
    int ans;
    cin >> ans;
    for (int i = 1; i < n; ++i) {
        int val;
        cin >> val;
        ans &= val;
    }
    cout << ans << endl;
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