// 25MCD005 WEEK-5 PROBLEM-E Petr and a Combination Lock
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for(int i = 0; i < n; ++i) cin >> a[i];

    bool found = false;
    for(int mask = 0; mask < (1 << n); ++mask) {
        int sum = 0;
        for(int i = 0; i < n; ++i) {
            if((mask >> i) & 1) sum += a[i];
            else sum -= a[i];
        }
        if(sum % 360 == 0) {
            found = true;
            break;
        }
    }

    if(found) cout << "YES" << endl;
    else cout << "NO" << endl;
    
    return 0;
}