#include <bits/stdc++.h>
using namespace std;

#define fastio ios::sync_with_stdio(false); cin.tie(NULL);

int main() {
    fastio;

    string s;
    
    cin >> s;
    
    cout << ((s.front() == s.back()) ? "Yes" : "No");
    
    return 0;
}