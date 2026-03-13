#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    int n;
    cin >> n;
    vector<int> divisors(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        for (int j = i; j <= n; j += i) {
            divisors[j]++;
        }
    }

    vector<long long> dp(n + 1);
    long long sum = 0;
    for (int i = 1; i <= n; i++) {
        dp[i] = (sum + divisors[i]) % MOD;
        sum = (sum + dp[i]) % MOD;
    }
    cout << dp[n] << endl;
    return 0;
}