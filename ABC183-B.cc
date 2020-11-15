#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <iomanip>
#define rep(i, N) for(int i = 0; i < N; ++i)
using namespace std;
using cor = pair<int, int>;
typedef long long ll;
const ll mod = 1000000007;

int main() {
    double sx, sy, gx, gy;
    cin >> sx >> sy >> gx >> gy;
    double g1;
    
    g1 = (sy*gx + sx*gy) / (gy + sy);
    cout << setprecision(9) << g1 << endl;

}