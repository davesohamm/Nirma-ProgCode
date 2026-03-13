// Problem - A, Karen and Test, 25MCD005 SOHAM DAVE
#include <iostream>
#include <vector>

using namespace std;

const long long MOD = 1e9 + 7;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

long long nCr(long long n, long long r, const vector<long long>& fact, const vector<long long>& invFact) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<long long> fact(n + 1, 1);
    vector<long long> invFact(n + 1, 1);
    for (int i = 1; i <= n; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[n] = modInverse(fact[n]);
    for (int i = n - 1; i >= 0; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }

    if (n % 4 == 0) {
        long long ans = 0;
        long long m = n / 2 - 1;
        for (int i = 0; i <= m; ++i) {
            long long C = nCr(m, i, fact, invFact);
            ans = (ans + a[2 * i] * C) % MOD;
            ans = (ans - a[2 * i + 1] * C) % MOD;
        }
        cout << (ans % MOD + MOD) % MOD << "\n";
    } else if (n % 4 == 1) {
        long long ans = 0;
        long long m = n / 2;
        for (int i = 0; i <= m; ++i) {
            long long C = nCr(m, i, fact, invFact);
            ans = (ans + a[2 * i] * C) % MOD;
        }
        cout << (ans % MOD + MOD) % MOD << "\n";
    } else if (n % 4 == 2) {
        long long ans = 0;
        long long m = n / 2 - 1;
        for (int i = 0; i <= m; ++i) {
            long long C = nCr(m, i, fact, invFact);
            ans = (ans + a[2 * i] * C) % MOD;
            ans = (ans + a[2 * i + 1] * C) % MOD;
        }
        cout << (ans % MOD + MOD) % MOD << "\n";
    } else if (n % 4 == 3) {
        vector<long long> b(n - 1);
        for (int i = 0; i < n - 1; ++i) {
            if (i % 2 == 0) b[i] = (a[i] + a[i + 1]) % MOD;
            else b[i] = (a[i] - a[i + 1]) % MOD;
        }
        long long ans = 0;
        long long m = (n - 1) / 2 - 1;
        for (int i = 0; i <= m; ++i) {
            long long C = nCr(m, i, fact, invFact);
            ans = (ans + b[2 * i] * C) % MOD;
            ans = (ans + b[2 * i + 1] * C) % MOD;
        }
        cout << (ans % MOD + MOD) % MOD << "\n";
    }
    return 0;
}