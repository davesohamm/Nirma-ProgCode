#include <iostream>
#include <vector>
#include <string>

using namespace std;

long long MOD = 998244353;

void solve() {
    string s;
    cin >> s;
    int n = s.length();

    long long min_ops = 0;
    long long ways = 1;
    
    int i = 0;
    while (i < n) {
        int j = i;
        while (j < n && s[j] == s[i]) {
            j++;
        }
        int block_len = j - i;
        min_ops += (block_len - 1);
        ways = (ways * block_len) % MOD;
        i = j;
    }

    for (int k = 1; k <= min_ops; k++) {
        ways = (ways * k) % MOD;
    }

    cout << min_ops << " " << ways << "\n";
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}