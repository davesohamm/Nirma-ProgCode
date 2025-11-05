// 25MCD005 SOHAM DAVE WEEK-1 PROBLEM-3 "TRAFFIC LIGHTS"
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long street_len;
    int n;
    cin >> street_len >> n;

    vector<long long> lights(n);
    for (int i = 0; i < n; i++) cin >> lights[i];

    set<long long> positions;
    multiset<long long> segments;

    positions.insert(0);
    positions.insert(street_len);
    segments.insert(street_len);

    for (int i = 0; i < n; i++) {
        long long pos = lights[i];

        auto it_right = positions.upper_bound(pos);
        auto it_left = prev(it_right);

        long long left = *it_left;
        long long right = *it_right;

        // remove old segment
        segments.erase(segments.find(right - left));

        // add new segments
        segments.insert(pos - left);
        segments.insert(right - pos);

        positions.insert(pos);

        // print current maximum segment
        cout << *segments.rbegin() << " ";
    }

    return 0;
}
