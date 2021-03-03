/*
     1     2     3     4     5
  |-----|-----|-----|-----|-----|
4 |     |     |     |     |     |
  |-----|-----|-----|-----|-----|
3 |     |     |     |     |     |
  |-----|-----|-----|-----|-----|
2 |  1  |     |     |     |     |
  |-----|-----|-----|-----|-----|
1 |  1  |  3  |  6  | 1 0 | 1 5 |
  |-----|-----|-----|-----|-----|
0 |  1  |  2  |  3  |  4  |  5  |
  |-----|-----|-----|-----|-----|
 */

//37442160
/*
 for(int i = 0; i < 15; i++){
     for(int j = 0; j < 15; j++){
         cout << arr[i][j] << " | ";
     }
     cout << endl;
 }
 */

#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    
    int arr[15][15] = {0};
    
    for(int i = 1; i < 15 ; i++){
        arr[0][i] = i;
        arr[i][0] = i;
    }
    
    int T,k,n;
    
    cin >> T;
    
    for(int i = 0; i < T; i++){
        cin >> k >> n;
        for(int j = 1; j <= k; j++){
            for(int l = 1; l <= n; l++){
                int sum = 0;
                for(int x = 1; x <= l; x++){
                    sum += arr[j-1][x];
                }
                arr[j][l] = sum;
            }
        }
        
        cout << arr[k][n] << endl;
    }
}
