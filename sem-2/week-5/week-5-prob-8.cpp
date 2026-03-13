// 25MCD005 WEEK-5 PROBLEM-H Dasha and Nightmares
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    vector<int> mask(n), parity(n);
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (char c : s) {
            int bit = c - 'a';
            mask[i] |= (1 << bit);
            parity[i] ^= (1 << bit);
        }
    }
    long long ans = 0;
    for (int skip = 0; skip < 26; skip++) {
        unordered_map<int, int> counts;
        int target = ((1 << 26) - 1) ^ (1 << skip);
        for (int i = 0; i < n; i++) {
            if (!((mask[i] >> skip) & 1)) {
                ans += counts[target ^ parity[i]];
                counts[parity[i]]++;
            }
        }
    }
    cout << ans << endl;
    return 0;
}