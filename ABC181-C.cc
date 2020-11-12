#include <iostream>
#include <vector>
#define rep(i, N) for(int i = 0; i < N; ++i)
using namespace std;
using cor = pair<int, int>;

int main() {
    int N;
    cin >> N;
    vector<cor> v(N);

    rep(i, N) cin >> v[i].first >> v[i].second;
    rep(i, N-2) {
        for(int j=i+1; j < N-1; ++j) {
            for(int k=j+1; k < N; ++k){
                if (v[j].first - v[i].first == 0){
                    if (v[k].first - v[i].first == 0){
                        cout << "Yes" << endl;
                        return 0;
                    }
                }
                else {
                    double ab = double(v[j].second - v[i].second) / double(v[j].first - v[i].first);
                    double ac = double(v[k].second - v[i].second) / double(v[k].first - v[i].first);
                    if (ab == ac) {
                        cout << "Yes" << endl;
                        return 0;
                    }
                }
            }
        }
    }
    cout << "No" << endl;
    return 0;
    
}