// Problem - C, Turn Off The TV, 25MCD005 SOHAM DAVE
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (!(cin >> n)) return 0;
    vector<pair<int, int>> segs(n);
    vector<int> pts;
    for (int i = 0; i < n; ++i) {
        cin >> segs[i].first >> segs[i].second;
        pts.push_back(segs[i].first);
        pts.push_back(segs[i].second);
        pts.push_back(segs[i].second + 1);
    }
    sort(pts.begin(), pts.end());
    pts.erase(unique(pts.begin(), pts.end()), pts.end());
    int m = pts.size();
    vector<int> diff(m + 1, 0);
    for (int i = 0; i < n; ++i) {
        int l = lower_bound(pts.begin(), pts.end(), segs[i].first) - pts.begin();
        int r = lower_bound(pts.begin(), pts.end(), segs[i].second + 1) - pts.begin();
        diff[l]++;
        diff[r]--;
    }
    vector<int> cov(m, 0);
    int cur = 0;
    for (int i = 0; i < m; ++i) {
        cur += diff[i];
        cov[i] = cur;
    }
    vector<int> pref(m + 1, 0);
    for (int i = 0; i < m; ++i) {
        pref[i + 1] = pref[i] + (cov[i] == 1 ? 1 : 0);
    }
    for (int i = 0; i < n; ++i) {
        int l = lower_bound(pts.begin(), pts.end(), segs[i].first) - pts.begin();
        int r = lower_bound(pts.begin(), pts.end(), segs[i].second) - pts.begin();
        if (pref[r + 1] - pref[l] == 0) {
            cout << i + 1 << "\n";
            return 0;
        }
    }
    cout << -1 << "\n";
    return 0;
}