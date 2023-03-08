#include <iostream>
#include <string>
#include <stack>

using std::cin;
using std::cout;
using std::endl;

using std::string;

using std::stack;


int main() {
    stack<int> s;
    string mode; cin >> mode;

    while (mode != "exit") {
        if (mode == "push") {
            int tmp; cin >> tmp;
            s.push(tmp);
            cout << "ok" << endl;

        } else if (mode == "pop") {
            if (!s.empty()) {
                cout << s.top() << endl;
                s.pop();
            }
            else cout << "error" << endl;

        } else if (mode == "back") {
            if (!s.empty()) cout << s.top() << endl;
            else cout << "error" << endl;

        } else if (mode == "size") {
            cout << s.size() << endl;

        } else if (mode == "clear") {
            s = stack<int>();
            cout << "ok" << endl;

        }
        cin >> mode;
    }

    cout << "bye" << endl;

    return 0;
}
