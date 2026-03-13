// 25MCD005 SOHAM DAVE Problem G - Almost Difference
#include <iostream>
#include <map>

using namespace std;

void print(__int128 n) {
    if (n < 0) {
        cout << "-";
        n = -n;
    }
    if (n > 9) print(n / 10);
    cout << (int)(n % 10);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (!(cin >> n)) return 0;
    __int128 ans = 0;
    long long current_sum = 0;
    map<long long, long long> counts;
    for (int i = 0; i < n; i++) {
        long long a;
        cin >> a;
        ans += (__int128)a * i - current_sum;
        auto it1 = counts.find(a - 1);
        if (it1 != counts.end()) {
            ans -= it1->second;
        }
        auto it2 = counts.find(a + 1);
        if (it2 != counts.end()) {
            ans += it2->second;
        }
        current_sum += a;
        counts[a]++;
    }
    print(ans);
    cout << "\n";
    return 0;
}