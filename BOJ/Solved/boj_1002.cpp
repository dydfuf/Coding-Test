#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int count;
    cin >> count;
    
    for(int i = 0; i < count; i++){
        int x1,y1, x2,y2, r1,r2;
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
        
        int dist = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1);
        int sum = (r1+r2)*(r1+r2);
        int diff = (r1-r2)*(r1-r2);
        
        if(dist == 0){
            if(diff == 0) cout << "-1" << '\n';
            else cout << "0" << '\n';
        }
        else if (dist == sum || dist == diff) cout << "1" << '\n';
        else if (dist > diff && dist < sum) cout << "2" << '\n';
        else cout << "0" << '\n';
    }
}
