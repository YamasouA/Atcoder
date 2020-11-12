#include <iostream>
#include <vector>
#include <cmath>
#define rep(i, N) for(int i = 0; i < N; ++i)
using namespace std;
using cor = pair<int, int>;
typedef long long ll;
const ll mod = 1000000007;



int main() {
    int N;
    cin >> N;
    vector<ll> v(N);
    vector<ll> s(N+1, 0);
    rep(i, N){
        cin >> v[i];
        s[i+1] = s[i] + v[i];
    } 

    ll ans=0;
    rep(i, N){
        ans += v[i] * ((s[N] - s[i+1]) % mod)%mod;
        ans %= mod;        
    }
    cout << ans << endl;
}