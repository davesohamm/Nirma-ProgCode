// 25MCD005 SOHAM DAVE Problem H - Buses
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long n, m;
    if (!(cin >> n >> m)) return 0;
    vector<pair<long long, long long>> buses(m);
    vector<long long> S;
    S.push_back(-1);
    S.push_back(0);
    S.push_back(n);
    for (int i = 0; i < m; i++) {
        cin >> buses[i].first >> buses[i].second;
        S.push_back(buses[i].first);
        S.push_back(buses[i].second);
    }
    sort(S.begin(), S.end());
    S.erase(unique(S.begin(), S.end()), S.end());
    vector<vector<long long>> ends_at(S.size());
    for (int i = 0; i < m; i++) {
        int t_idx = lower_bound(S.begin(), S.end(), buses[i].second) - S.begin();
        ends_at[t_idx].push_back(buses[i].first);
    }
    vector<long long> dp(S.size(), 0);
    vector<long long> pref(S.size(), 0);
    long long MOD = 1000000007;
    for (int i = 0; i < S.size(); i++) {
        if (S[i] == -1) {
            pref[i] = 0;
        } else if (S[i] == 0) {
            dp[i] = 1;
            pref[i] = (pref[i - 1] + dp[i]) % MOD;
        } else {
            long long current_dp = 0;
            for (long long s : ends_at[i]) {
                int s_idx = lower_bound(S.begin(), S.end(), s) - S.begin();
                long long contrib = (pref[i - 1] - pref[s_idx - 1] + MOD) % MOD;
                current_dp = (current_dp + contrib) % MOD;
            }
            dp[i] = current_dp;
            pref[i] = (pref[i - 1] + dp[i]) % MOD;
        }
    }
    int n_idx = lower_bound(S.begin(), S.end(), n) - S.begin();
    cout << dp[n_idx] << "\n";
    return 0;
}