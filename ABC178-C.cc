#include <iostream>
#include <vector>
#include <cmath>
#define rep(i, N) for(int i = 0; i < N; ++i)
using namespace std;
using cor = pair<int, int>;
typedef long long ll;
const ll mod = 1000000007;

ll powmod(ll x, ll y) {
    ll res = 1;
    for(ll i=0; i<y; i++) {
        res = res*x % mod;
    }
    return res;
}

int main() {
    ll n;
    cin >> n;
    //0が一つもない
    ll ans = powmod(10, n) - powmod(9, n) - powmod(9, n) + powmod(8, n);
    //負の場合の対策(正なら何も変わらない)
    ans %= mod;
    ans = (ans + mod) % mod;
    cout << ans << endl;
}