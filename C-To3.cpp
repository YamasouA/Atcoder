#include <iostream>
#include <string>
#include <vector>
#define rep(i, n) for (int i = 0; i < n; ++i)
using namespace std;

const int INF = 10000000;

int main() {
    string s;
    cin >> s;
    int n =s.size();
    vector<int> c(3);
    //割ったあまり0, 1, 2がそれぞれ何個あるか
    rep(i, n) c[(s[i] - '0')%3]++;
    int x = 0;
    //あまりの和を調べる
    rep(i, 3) x += c[i] * i;
    int ans = INF;
    //余りが１を消す数i1, 余りが2を消す数i2
    rep(i1, 3)rep(i2, 3){
        //最初にカウントした数より消す数が多いときは抜く
        if (c[1] < i1) continue;
        if (c[2] < i2) continue;
        //すべて消すのはなし
        if (i1 + i2 == n) continue;
        int nx =x;
        nx -= i1 * 1;
        nx -= i2 * 2;
        if (nx % 3 == 0) ans = min(ans, i1+i2); 
    }
    if (ans == INF) ans = -1;
    cout << ans << endl;
    return 0;
}