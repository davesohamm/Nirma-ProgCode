// 25MCD005 WEEK-4 PROBLEM-E Permutations & Primes
#include <iostream>
#include <vector>

using namespace std;

void solve() {
    int n;
    cin >> n;
    if (n == 1) {
        cout << 1 << endl;
        return;
    }
    if (n == 2) {
        cout << "2 1" << endl;
        return;
    }
    vector<int> a(n);
    a[0] = 2;
    a[n / 2] = 1;
    a[n - 1] = 3;
    int cur = 4;
    for (int i = 0; i < n; ++i) {
        if (a[i] == 0) {
            a[i] = cur++;
        }
    }
    for (int i = 0; i < n; ++i) {
        cout << a[i] << (i == n - 1 ? "" : " ");
    }
    cout << endl;
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