// 25MCD005 SOHAM DAVE Problem F - The Kamphaeng Phet's Chedis
#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <algorithm>

using namespace std;

void solve() {
    int N, M;
    double K;
    if (!(cin >> N >> M >> K)) return;
    string a, b;
    cin >> a >> b;
    vector<double> dp(M + 2, 0.0);
    vector<double> rect_sum(M + 2, 0.0);
    vector<double> next_dp(M + 2, 0.0);
    for (int i = N + 1; i >= 1; i--) {
        if (i == N + 1) {
            dp[M + 1] = 0;
            double current_suffix_sum = 0;
            for (int j = M; j >= 1; j--) {
                current_suffix_sum += dp[j + 1];
                dp[j] = min(1.0 + dp[j + 1], K + current_suffix_sum / (M - j + 1.0));
            }
            double suffix_for_rect = 0;
            for (int j = M + 1; j >= 1; j--) {
                suffix_for_rect += dp[j];
                rect_sum[j] = suffix_for_rect;
            }
        } else {
            next_dp = dp;
            dp[M + 1] = min(1.0 + next_dp[M + 1], K + rect_sum[M + 1] / (N - i + 1.0));
            for (int j = M; j >= 1; j--) {
                if (a[i - 1] == b[j - 1]) {
                    dp[j] = next_dp[j + 1];
                } else {
                    double opt2 = 1.0 + next_dp[j];
                    double opt3 = 1.0 + dp[j + 1];
                    double opt4 = K + rect_sum[j + 1] / ((N - i + 1.0) * (M - j + 1.0));
                    dp[j] = min({opt2, opt3, opt4});
                }
            }
            double suffix_for_rect = 0;
            for (int j = M + 1; j >= 1; j--) {
                suffix_for_rect += dp[j];
                rect_sum[j] += suffix_for_rect;
            }
        }
    }
    cout << fixed << setprecision(10) << dp[1] << "\n";
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