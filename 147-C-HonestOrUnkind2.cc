#include <iostream>
#include <vector>
#define rep(i, n)  for(int i=0; i < n; ++i)
using namespace std;

//1つの証言を表す構造体
using pint = pair<int, int>; //人と[0 or 1]

//入力
int N;
vector<vector<pint>> v;

//bitによる決め打ち
bool judge(int bit) {

    //i人目の証言
    rep(i, N) {
        if (!(bit&(1 << i))) continue; //i番目が不親切なら証言は無意味
        //i番目の発言をすべてチェック
        for (pint xy : v[i]) {
            int x = xy.first;
            int y = xy.second;

            //y=1なのに不親切はダメ
            if (y == 1 && !(bit & (1 << x))) return false;

            //y=0なのに正直者はダメ
            if (y == 0 && (bit & (1 << x))) return false;
        }
    }
    return true;
}

int main() {
    cin >> N;
    v.resize(N);
    rep(i, N) {
        int A;
        cin >> A;
        v[i].resize(A);
        rep(j, A) {
            cin >> v[i][j].first >> v[i][j].second;
            --v[i][j].first; //0-indexにする
        }
    }

    int res = 0;
    for (int bit = 0; bit < (1 << N); ++bit) {

        //矛盾あるか
        if (judge(bit)) {

            //bitに含まれる人数数える
            int count = 0;
            rep(i, N) {
                if (bit & (1 << i)) ++count;
            }
            res = max(res, count);
        }
    }
    cout << res << endl;
}
