// 25MCD005 PROBLEM E - Alternating Subsequence
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<long long> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];
        long long sum = 0;
        int i = 0;
        while (i < n) {
            long long cur_max = a[i];
            int j = i;
            while (j < n && ((a[i] > 0 && a[j] > 0) || (a[i] < 0 && a[j] < 0))) {
                cur_max = max(cur_max, a[j]);
                j++;
            }
            sum += cur_max;
            i = j;
        }
        cout << sum << endl;
    }
    return 0;
}