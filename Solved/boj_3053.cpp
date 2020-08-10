#include <iostream>

#define pie 3.14159265358979

using namespace std;

int main(int argc, const char * argv[]) {
    
    int input;
    cin >> input;
    
    double origin = pie*input*input;
    double taxi = 2*input*input;
    
    cout.setf(ios::fixed);
    cout.precision(6);
    cout << origin << '\n' << taxi;
}
