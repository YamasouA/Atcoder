#include <iostream>
#include <vector>
#include <cmath>
#define rep(i, N) for(int i = 0; i < N; ++i)
using namespace std;
using cor = pair<int, int>;
typedef long long ll;
const ll mod = 1000000007;

int main() {
    ll n;
    cin >> n;
    vector<ll> v(n);
    rep(i, n) cin >> v[i];

    ll sum = 0;
    rep(i, n-1) {
        if (v[i] > v[i+1]) { 
            sum += (v[i] - v[i+1]);
            v[i+1] += v[i] - v[i+1];
        }
    }
    cout << sum << endl;
}