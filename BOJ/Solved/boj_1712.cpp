#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int A,B,C;
    
    cin >> A >> B >> C;
    
    // A + Bx < Cx
    // A(C-B) < x
    
    if(B >= C) cout << "-1";
    else cout << A/(C-B) + 1;
}
