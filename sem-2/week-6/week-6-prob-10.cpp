// Problem - J - Tokitsukaze and Strange Rectangle - 25MCD005 SOHAM DAVE
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}
    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }
    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    if (!(cin >> n)) return 0;
    
    vector<pair<int, int>> points(n);
    vector<int> xs(n);
    for (int i = 0; i < n; ++i) {
        cin >> points[i].first >> points[i].second;
        xs[i] = points[i].first;
    }
    
    sort(xs.begin(), xs.end());
    xs.erase(unique(xs.begin(), xs.end()), xs.end());
    int u = xs.size();
    
    for (int i = 0; i < n; ++i) {
        points[i].first = lower_bound(xs.begin(), xs.end(), points[i].first) - xs.begin() + 1;
    }
    
    sort(points.begin(), points.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        if (a.second != b.second) return a.second > b.second;
        return a.first < b.first;
    });
    
    Fenwick fenwick(u);
    vector<bool> in_tree(u + 1, false);
    long long ans = 0;
    
    int i = 0;
    while (i < n) {
        int j = i;
        vector<int> current_xs;
        while (j < n && points[j].second == points[i].second) {
            current_xs.push_back(points[j].first);
            j++;
        }
        
        for (int x : current_xs) {
            if (!in_tree[x]) {
                fenwick.add(x, 1);
                in_tree[x] = true;
            }
        }
        
        long long total_active = fenwick.query(u);
        ans += total_active * (total_active + 1) / 2;
        
        long long count0 = fenwick.query(current_xs[0] - 1);
        ans -= count0 * (count0 + 1) / 2;
        
        for (size_t k = 0; k < current_xs.size() - 1; ++k) {
            long long count_k = fenwick.query(current_xs[k+1] - 1) - fenwick.query(current_xs[k]);
            ans -= count_k * (count_k + 1) / 2;
        }
        
        long long count_last = fenwick.query(u) - fenwick.query(current_xs.back());
        ans -= count_last * (count_last + 1) / 2;
        
        i = j;
    }
    
    cout << ans << "\n";
    return 0;
}