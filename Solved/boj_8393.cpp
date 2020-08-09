#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int x, sum = 0;
    
    cin >> x;
    
    for(int i = 0; i <= x; i++){
        sum += i;
    }
    
    cout << sum;
}
