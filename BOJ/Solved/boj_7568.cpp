#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int N;
    cin >> N;
    
    int arr[N+1][3];
    
    for(int i = 0; i < N; i++){
        int W,H;
        cin >> W >> H;
        arr[i][0] = W;
        arr[i][1] = H;
        arr[i][2] = 1;
    }
    
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if((arr[i][0] < arr[j][0]) && (arr[i][1] < arr[j][1])) arr[i][2]++;
        }
    }
    
    for(int i = 0; i < N; i++){
        cout << arr[i][2] << " "
        ;
    }
    
}
