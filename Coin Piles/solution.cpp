#include <iostream>
#include <cmath>

using namespace std;

bool solve(uint64_t a, uint64_t b) {
    return (a+b) % 3 == 0 && max(a, b) <= 2 * min(a, b);
}


int main() {
    uint64_t t, a, b;
    cin >> t;
    for (uint64_t i = 0; i < t; i++) {
        cin >> a >> b;
        cout << (solve(a, b) ? "YES" : "NO") << '\n';
    }
}
