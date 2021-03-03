#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int T;
    
    cin >> T;
    
    for(int i = 0; i < T; i++){
        int H, W, N;
        
        cin >> H >> W >> N;
        
        int floor,room_number;
        
        if(N%H == 0){
            floor = H;
            room_number = N/H;
        }
        else{
            floor = N%H;
            room_number = N/H+1;
        }
        
        cout << floor*100+room_number << endl;
    }
}
