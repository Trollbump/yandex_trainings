#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;

using std::string;

int main() {
    int k; cin >> k;
    string s; cin >> s;
    char alph[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    int max_b = 0;

    for (char c : alph) {
        int r = 0;
        int cnt = k;
        int b = 0;
        
        for (int l = 0; l < s.length(); ++l) {
            while ((r < s.length()) && (cnt >= 0)) {
                if (s[r] == c) {
                    ++b;
                    ++r;
                } else {
                    if (cnt > 0) {
                        --cnt;
                        ++b;
                        ++r;
                    } else {
                        break;
                    }
                }
            }
            if (max_b < b) max_b = b;

            if (r == s.length()) --r;

            if (s[l] == c) {
                --b;
            } else {
                ++cnt;
                --b;
            }
        }
    }

    cout << max_b << endl;

	return 0;
}
