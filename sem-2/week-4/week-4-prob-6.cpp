// 25MCD005 WEEK-4 PROBLEM-F Rudolph and Christmas Tree
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

void solve() {
    int n;
    long long d, h;
    cin >> n >> d >> h;
    vector<long long> y(n);
    for (int i = 0; i < n; ++i) {
        cin >> y[i];
    }
    long double area = 0.0;
    long double triangle_area = 0.5 * d * h;
    for (int i = 0; i < n - 1; ++i) {
        if (y[i + 1] >= y[i] + h) {
            area += triangle_area;
        } else {
            long double h_diff = y[i + 1] - y[i];
            long double h_small = h - h_diff;
            long double d_small = (long double)d * h_small / h;
            long double small_area = 0.5 * d_small * h_small;
            area += (triangle_area - small_area);
        }
    }
    area += triangle_area;
    cout << fixed << setprecision(7) << area << endl;
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