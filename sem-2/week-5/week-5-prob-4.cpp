// 25MCD005 WEEK-5 PROBLEM-D AND 0, Sum Big
#include <iostream>

using namespace std;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= 1000000007;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % 1000000007;
        base = (base * base) % 1000000007;
        exp /= 2;
    }
    return res;
}

void solve() {
    int n, k;
    cin >> n >> k;
    cout << power(n, k) << endl;
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