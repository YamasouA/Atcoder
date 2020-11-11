#include <iostream>
#include <vector>
#define rep(i, N) for(int i = 0; i < N; ++i)
using namespace std;

int main() {
    int N;
    cin >> N;
    int ans = 0;
    for (int i = 1; i < N; ++i) {
        ans += (N - 1) / i;
    }
    cout << ans << endl;
}