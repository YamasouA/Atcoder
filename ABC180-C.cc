#include <iostream>
#include <set>
using namespace std;

int main() {
    long n;
    cin >> n;

    set<long> ans;
    for (long d=1; d*d<=n; d++) {
        if (n%d==0) {
            ans.insert(d);
            ans.insert(n/d);
        }
    }
    for(auto x: ans) cout << x << endl;
}