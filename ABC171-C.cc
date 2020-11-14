#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#define rep(i, N) for(int i = 0; i < N; ++i)
using namespace std;
using cor = pair<int, int>;
typedef long long ll;
const ll mod = 1000000007;

int main() {
    ll n;
    cin >> n;
    string res = "";
    while (n) {
        --n;
        res += (char)('a' + (n%26));
        n /= 26;
    }
    reverse(res.begin(), res.end());
    cout << res << endl;
}