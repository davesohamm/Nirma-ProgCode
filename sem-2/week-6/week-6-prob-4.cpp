// Problem - D, Hanoi Factory, 25MCD005 SOHAM DAVE
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Ring {
    int a, b;
    long long h;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (!(cin >> n)) return 0;
    vector<Ring> rings(n);
    vector<int> pts;
    for (int i = 0; i < n; ++i) {
        cin >> rings[i].a >> rings[i].b >> rings[i].h;
        pts.push_back(rings[i].a);
        pts.push_back(rings[i].b);
    }
    sort(pts.begin(), pts.end());
    pts.erase(unique(pts.begin(), pts.end()), pts.end());
    sort(rings.begin(), rings.end(), [](const Ring& x, const Ring& y) {
        if (x.b != y.b) return x.b > y.b;
        return x.a > y.a;
    });
    int m = pts.size();
    vector<long long> bit(m + 1, 0);
    auto update = [&](int idx, long long val) {
        for (; idx <= m; idx += idx & -idx) {
            bit[idx] = max(bit[idx], val);
        }
    };
    auto query = [&](int idx) {
        long long res = 0;
        for (; idx > 0; idx -= idx & -idx) {
            res = max(res, bit[idx]);
        }
        return res;
    };
    long long max_ans = 0;
    for (int i = 0; i < n; ++i) {
        int a_idx = lower_bound(pts.begin(), pts.end(), rings[i].a) - pts.begin() + 1;
        int b_idx = lower_bound(pts.begin(), pts.end(), rings[i].b) - pts.begin() + 1;
        long long val = rings[i].h + query(b_idx - 1);
        max_ans = max(max_ans, val);
        update(a_idx, val);
    }
    cout << max_ans << "\n";
    return 0;
}