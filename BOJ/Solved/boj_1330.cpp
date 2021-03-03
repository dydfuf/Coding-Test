#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    
    int a, b;
    
    cin >> a >> b;
    
    if(a > b){
        cout << ">" << endl;
    }
    else if(a < b){
        cout << "<" << endl;
    }
    else if(a == b){
        cout << "==" << endl;
    }
}
