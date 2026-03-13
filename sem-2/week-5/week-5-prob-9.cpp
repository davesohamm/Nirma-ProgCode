// 25MCD005 WEEK-5 PROBLEM-I Don't Blame Me
#include <iostream>
#include <vector>

using namespace std;

void solve() {
    int n, k;
    if (!(cin >> n >> k)) return;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<long long> dp(64, 0);
    const long long MOD = 1e9 + 7;

    for (int x : a) {
        vector<long long> next_dp = dp;
        for (int mask = 0; mask < 64; ++mask) {
            if (dp[mask] > 0) {
                int new_mask = mask & x;
                next_dp[new_mask] = (next_dp[new_mask] + dp[mask]) % MOD;
            }
        }
        next_dp[x] = (next_dp[x] + 1) % MOD;
        dp = next_dp;
    }

    long long ans = 0;
    for (int mask = 0; mask < 64; ++mask) {
        if (__builtin_popcount(mask) == k) {
            ans = (ans + dp[mask]) % MOD;
        }
    }
    cout << ans << "\n";
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