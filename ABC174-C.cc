#include <iostream>
#include <vector>
#include <cmath>
#define rep(i, N) for(int i = 0; i < N; ++i)
using namespace std;
using cor = pair<int, int>;
typedef long long ll;
const ll mod = 1000000007;

int main() {
    ll k;
    cin >> k;
    ll seven = 0;
    bool flag = true;
    if (k%2 == 0) cout << "-1" << endl;
    else{
        rep(i, 1000000) {
        if (i == 0) seven += 7;
        else seven = seven * 10 + 7;
        //cout << seven << endl;
        seven %= k;
        //cout << seven << endl;
        if (seven == 0) {
            cout << i+1 << endl;
            flag = false;
            break;
        }
        
    }
    if (flag) cout << "-1" << endl;
    }
}
    