#include <iostream>
#include <algorithm>

using namespace std;

long long gcd(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

long long lcm(long long a, long long b) {
    return (a / gcd(a, b)) * b;
}

int main() {
    long long x;
    cin >> x;
    long long ans = x;
    for (long long i = 1; i * i <= x; i++) {
        if (x % i == 0) {
            if (lcm(i, x / i) == x) {
                ans = min(ans, max(i, x / i));
            }
        }
    }
    cout << x / ans << " " << ans << endl;
    return 0;
}