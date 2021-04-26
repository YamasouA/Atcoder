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
    int x, n;
    cin >> x >> n;
    int ans_min = 1000;
    int min = 0;
    int ans = 0;
    vector<int> p(n), v(101);
    rep(i, 101) v[i] = i;
    rep(i, n) {
        cin >> p[i];
        v[p[i]] = -1;
    }

    if (n == 0) {
        cout << x << endl;
        return 0;
    }

    rep(i, 101) {
        if (v[i] == -1) continue;
        else {
            min = abs(x - v[i]);
            if (min < ans_min) {
                ans = v[i];
                ans_min = min;
            }
        }
    }
    cout << ans << endl;
}