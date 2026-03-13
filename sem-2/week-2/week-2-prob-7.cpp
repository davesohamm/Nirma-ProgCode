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
    long long n, k;
    cin >> n >> k;
    long long MOD = 1000000007;
    if (k == 0) {
        cout << 1 << endl;
        return;
    }
    long long even_ways = power(2, n - 1);
    if (n % 2 == 1) {
        cout << power(even_ways + 1, k) << endl;
    } else {
        long long ans = 0;
        long long current_ways = 1;
        for (int i = 0; i < k; i++) {
            long long remaining = power(power(2, n), k - 1 - i);
            ans = (ans + current_ways * remaining) % MOD;
            current_ways = (current_ways * (even_ways - 1 + MOD)) % MOD;
        }
        ans = (ans + current_ways) % MOD;
        cout << ans << endl;
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}