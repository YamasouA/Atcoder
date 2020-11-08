#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, m;
    cin >> N;
    vector<int> v(N);
    for (int i = 0; i < N; ++i) cin >> v[i];
    m = *max_element(v.begin(), v.end());
    int max = 0;
    int max_i = 0;
    for (int i = 2; i <= m; ++i) {
        int cnt = 0;
        for ( int j = 0; j < N; ++j) {
            if (v[j] % i == 0) cnt++;
        }
        //cout << i << max << cnt << endl;
        if (cnt >= max) {
            max = cnt;
            max_i = i;
        }
    }
    cout << max_i << endl;

}