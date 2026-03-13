// 25MCD005 WEEK-5 PROBLEM-G Candy Party (Easy Version)
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

bool solve() {
    int n;
    cin >> n;
    vector<long long> a(n);
    long long sum = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        sum += a[i];
    }
    if (sum % n != 0) return false;
    long long avg = sum / n;
    vector<int> give(32, 0), receive(32, 0);
    for (int i = 0; i < n; i++) {
        long long diff = abs(avg - a[i]);
        if (diff == 0) continue;
        long long x = -1, y = -1;
        for (int p = 0; p < 31; p++) {
            long long val = (1LL << p);
            if (__builtin_popcountll(diff + val) == 1) {
                x = p;
                y = __builtin_ctzll(diff + val);
                break;
            }
        }
        if (x == -1) return false;
        if (a[i] > avg) {
            give[y]++;
            receive[x]++;
        } else {
            give[x]++;
            receive[y]++;
        }
    }
    for (int i = 0; i < 32; i++) {
        if (give[i] != receive[i]) return false;
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--) {
        if (solve()) cout << "Yes\n";
        else cout << "No\n";
    }
    return 0;
}