#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int count;
    
    int x,y;
    
    cin >> count;
    
    
    for(int i = 0; i < count; i++){
        cin >> x >> y;
        cout << "Case #" << i+1 << ": " << x+y << endl;
    }
}
