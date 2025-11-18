// 25MCD005 SOHAM DAVE WEEK-9 PROBLEM-8 "Projects"
#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;

// Define a struct to hold project details
struct Project {
    long long end;
    long long start;
    long long reward;

    // Overload the less-than operator to sort by end time
    bool operator<(const Project& other) const {
        return end < other.end;
    }
};

int main() {
    // Optimize C++ standard input/output
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<Project> projects(n);
    for (int i = 0; i < n; ++i) {
        // Read as (start, end, reward)
        cin >> projects[i].start >> projects[i].end >> projects[i].reward;
    }

    // Sort projects based on their end day
    sort(projects.begin(), projects.end());

    // dp_ends will store the end days of projects in the optimal solution
    // dp_profits will store the corresponding maximum profit
    vector<long long> dp_ends = {0};
    vector<long long> dp_profits = {0};

    for (int i = 0; i < n; ++i) {
        long long a = projects[i].start;
        long long b = projects[i].end;
        long long p = projects[i].reward;

        // Find the latest project in dp that finishes before this one starts
        // lower_bound finds the first element NOT LESS than 'a'
        auto it = lower_bound(dp_ends.begin(), dp_ends.end(), a);
        
        // We need the element just before it
        int j = distance(dp_ends.begin(), it) - 1;

        long long profit = dp_profits[j] + p;

        // If this new profit is better than the last max profit,
        // it forms a new optimal point.
        if (profit > dp_profits.back()) {
            dp_ends.push_back(b);
            dp_profits.push_back(profit);
        }
    }

    // The answer is the maximum profit found
    cout << dp_profits.back() << "\n";

    return 0;
}