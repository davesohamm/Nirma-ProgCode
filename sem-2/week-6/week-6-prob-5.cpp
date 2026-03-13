// 25MCD005 SOHAM DAVE Problem E - Pashmak and Parmida's problem
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct FenwickTree {
    vector<int> bit;
    int n;
    FenwickTree(int n) {
        this->n = n;
        bit.assign(n + 1, 0);
    }
    void add(int idx, int val) {
        for (; idx <= n; idx += idx & -idx)
            bit[idx] += val;
    }
    int sum(int idx) {
        int ret = 0;
        for (; idx > 0; idx -= idx & -idx)
            ret += bit[idx];
        return ret;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (!(cin >> n)) return 0;
    vector<int> a(n), b(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        b[i] = a[i];
    }
    sort(b.begin(), b.end());
    b.erase(unique(b.begin(), b.end()), b.end());
    for (int i = 0; i < n; i++) {
        a[i] = lower_bound(b.begin(), b.end(), a[i]) - b.begin();
    }
    vector<int> freqL(b.size(), 0), freqR(b.size(), 0);
    vector<int> L(n), R(n);
    for (int i = 0; i < n; i++) {
        freqL[a[i]]++;
        L[i] = freqL[a[i]];
    }
    for (int i = n - 1; i >= 0; i--) {
        freqR[a[i]]++;
        R[i] = freqR[a[i]];
    }
    FenwickTree bit(n);
    long long ans = 0;
    for (int j = n - 1; j >= 0; j--) {
        ans += bit.sum(L[j] - 1);
        bit.add(R[j], 1);
    }
    cout << ans << "\n";
    return 0;
}