#include <iostream>
#include <cmath>

using namespace std;

bool solve(unsigned long long int a, unsigned long long int b) {
    return (a+b) % 3 == 0 && (a > b ? a <= 2 * b : a < b ? b <= 2 * a : 1);
}


int main() {
    unsigned long long int t, a, b;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> a >> b;
         if (solve(a, b)) cout << "YES";
         else cout << "NO";
    }
}