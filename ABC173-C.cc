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
    int h, w, k;
    cin >> h >> w >> k;
    vector<string> v(h);
    int count = 0;
    int ans = 0;

    rep(i, h) cin >> v[i];

    for(int bit_h=0; bit_h<(1<<h); ++bit_h){
        for(int bit_w=0; bit_w<(1<<w); ++bit_w){
            count = 0;
            rep(i, h)rep(j, w) {
                if ((bit_h & (1<<i)) | (bit_w & (1<<j))) {
                    
                }
                else{
                    if(v[i][j] =='#') count++;
                }
            }

            if (count == k) ans++;
        
        }
    }
    cout << ans << endl;

}