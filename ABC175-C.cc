#include <iostream>
#include <vector>
#include <cmath>
#define rep(i, N) for(int i = 0; i < N; ++i)
using namespace std;
using cor = pair<int, int>;
typedef long long ll;
const ll mod = 1000000007;

int main() {
    ll x, k, d;
    cin >> x >> k >> d;
    x = abs(x);
    
    ll ans;
    ll z = x / d;

    if (z >= k) {
        ans = abs(abs(x) - abs(k*d));
    }
    else {
        if ((k - z) % 2 == 0) {
            ans = abs(abs(x) - abs(z*d));
        } 
        else ans = abs(abs(x) - abs((z+1)*d));
    }
    cout << ans << endl;
}