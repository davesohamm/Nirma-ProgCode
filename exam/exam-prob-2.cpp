// 25MCD005 EXAM-PROBLEM-2
/*
Problem: Apartments

There are n applicants and m free apartments. Your task is to distribute the apartments
so that as many applicants as possible will get an apartment.

Each applicant has a desired apartment size, and they will accept any apartment whose
size is close enough to the desired size. If an applicant's desired size is x, they will
accept any apartment with size in the range [x - k, x + k].

Input:
- The first line contains integers n, m, and k:
    n = number of applicants
    m = number of apartments
    k = maximum allowed size difference

- The second line contains n integers a1, a2, ..., an:
    a[i] = desired apartment size of applicant i

- The third line contains m integers b1, b2, ..., bm:
    b[i] = size of apartment i

Output:
- Print one integer: the number of applicants who will get an apartment.

Constraints:
1 ≤ n, m ≤ 2 * 10^5
0 ≤ k ≤ 10^9
1 ≤ a[i], b[i] ≤ 10^9

Example:
Input:
    4 3 5
    60 45 80 60
    30 60 75
Output:
    2
*/


#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

void solve() {
    long long n, m, k;
    if (!(cin >> n >> m >> k)) return;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<long long> b(m);
    for (int i = 0; i < m; ++i) {
        cin >> b[i];
    }
    
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int i = 0;
    int j = 0;
    int count = 0;

    while (i < n && j < m) {
        if (abs(a[i] - b[j]) <= k) {
            count++;
            i++;
            j++;
        } else if (a[i] < b[j]) {
            i++;
        } else {
            j++;
        }
    }

    cout << count << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();

    return 0;
}