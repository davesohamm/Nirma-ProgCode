// 25MCD005 SOHAM DAVE WEEK-5 PROBLEM-1 "Word Capitalization"
#include <iostream>
#include <string>
using namespace std;

int main() {
    string word;
    cin >> word;
    word[0] = toupper(word[0]);
    cout << word;
    return 0;
}
