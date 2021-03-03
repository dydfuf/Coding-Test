#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int h,m;
    
    cin >> h >> m;
    
    int modified_min = m - 45;
    if(modified_min < 0){
        h = h-1;
        if(h<0) h = h + 24;
        modified_min = modified_min +60;
    }
    
    cout << h << endl << modified_min << endl;
}
