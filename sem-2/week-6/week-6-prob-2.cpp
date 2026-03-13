// Problem - B, Longest Regular Bracket Sequence, 25MCD005 SOHAM DAVE
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s;
    if (!(cin >> s)) return 0;
    int n = s.length();
    vector<int> dp(n, 0);
    int max_len = 0;
    int count = 1;
    for (int i = 1; i < n; ++i) {
        if (s[i] == ')') {
            if (s[i - 1] == '(') {
                dp[i] = 2 + (i >= 2 ? dp[i - 2] : 0);
            } else if (i - dp[i - 1] - 1 >= 0 && s[i - dp[i - 1] - 1] == '(') {
                dp[i] = dp[i - 1] + 2 + (i - dp[i - 1] - 2 >= 0 ? dp[i - dp[i - 1] - 2] : 0);
            }
            if (dp[i] > max_len) {
                max_len = dp[i];
                count = 1;
            } else if (dp[i] == max_len && max_len > 0) {
                count++;
            }
        }
    }
    if (max_len == 0) count = 1;
    cout << max_len << " " << count << "\n";
    return 0;
}