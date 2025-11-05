// 25MCD005 SOHAM DAVE WEEK-6 PROBLEM-8 "Interesting Array"
#include <iostream>
#include <vector>
#include <cmath>
#include <tuple>

using namespace std;

int query_and(int L, int R, const vector<vector<int>>& st, const vector<int>& logs) {
    int length = R - L + 1;
    int k = logs[length];
    return st[k][L] & st[k][R - (1 << k) + 1];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<tuple<int, int, int>> constraints(m);
    for (int i = 0; i < m; ++i) {
        cin >> get<0>(constraints[i]) >> get<1>(constraints[i]) >> get<2>(constraints[i]);
    }

    vector<int> ans(n, 0);

    for (int k = 0; k < 30; ++k) {
        vector<int> diff(n + 1, 0);
        for (int i = 0; i < m; ++i) {
            int l, r, q;
            tie(l, r, q) = constraints[i];
            if ((q >> k) & 1) {
                diff[l - 1]++;
                if (r < n) {
                    diff[r]--;
                }
            }
        }

        int cover = 0;
        for (int i = 0; i < n; ++i) {
            cover += diff[i];
            if (cover > 0) {
                ans[i] |= (1 << k);
            }
        }
    }

    vector<int> logs(n + 1);
    logs[1] = 0;
    for (int i = 2; i <= n; ++i) {
        logs[i] = logs[i / 2] + 1;
    }

    int K = logs[n];
    vector<vector<int>> st(K + 1, vector<int>(n));

    for (int i = 0; i < n; ++i) {
        st[0][i] = ans[i];
    }

    for (int k = 1; k <= K; ++k) {
        for (int i = 0; i + (1 << k) <= n; ++i) {
            st[k][i] = st[k - 1][i] & st[k - 1][i + (1 << (k - 1))];
        }
    }

    for (int i = 0; i < m; ++i) {
        int l, r, q;
        tie(l, r, q) = constraints[i];
        if (query_and(l - 1, r - 1, st, logs) != q) {
            cout << "NO\n";
            return 0;
        }
    }

    cout << "YES\n";
    for (int i = 0; i < n; ++i) {
        cout << ans[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}
