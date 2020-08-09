/*
 거리 : 1 -> 1
 거리 : 2 -> 11
 거리 : 3 -> 111
 거리 : 4 -> 121
 거리 : 5 -> 1121
 거리 : 6 -> 1221
 거리 : 7 -> 11221
 거리 : 8 -> 12221
 거리 : 9 -> 12321
 */
/*
 자료형 주의 int는 불가
 */

#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int count;
    cin >> count;
    
    for(int i = 0; i < count; i++){
        long long x, y;
        cin >> x >> y;
        
        long long dis = y - x;
        double t = 0;
        for(double j = 0; ; j++){
            if(dis >= j*j && dis < (j+1)*(j+1)){
                t = j;
                break;
            }
        }
        
        if(dis > t*t && dis <= ((t+1)*(t+1) + t*t)/2){
            cout << 2*t << endl;
        }
        else if(dis > ((t+1)*(t+1) + t*t)/2 && dis < (t+1)*(t+1)){
            cout << 2*t + 1 << endl;
        }
        else if(dis == t*t){
            cout << 2*t - 1 << endl;
        }
    }
}
