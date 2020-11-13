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
    ll n, m, k;
    cin >> n >> m >> k;
    vector<ll> a(n), b(m), A(n+1), B(m+1);
    

    rep(i, n) cin >> a[i];
    rep(i, m) cin >> b[i];
    A[0] = 0;
    B[0] = 0;
    rep(i, n+1) {
        if (i == 0) A[i] = 0;
        else A[i] = a[i-1] + A[i-1];
        //cout << A[i] << endl;
    }
    rep(i , m+1) {
        if (i == 0) B[i] = 0;
        else B[i] = b[i-1] + B[i-1];
        //cout << B[i] << endl;
    }

    ll ans= 0,  j = m;

    rep(i, n+1) {
        if (A[i] > k) break;
        while (B[j] > k - A[i]){
            j--;
        }
        ans = max(ans, i+j);
    }
    cout << ans << endl;
}