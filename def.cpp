#include <iostream>
#include <vector>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; ++i)

int main() {
    int N;
    cin >> N;
    vector<int> v(N);
    rep(i, N) cin >> v[i];
    rep(i, N) cout << v[i];
}