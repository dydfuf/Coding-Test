/*

 Level-3 계단 오르기

 계단을 오르려 합니다. 계단의 개수는 n개이며 한번 오를 때 1 혹은 2칸씩 오를 수 있습니다. N개의 계단을 오를 때 몇가지 방법으로 다 오를 수 있습니까?
 
 계단은 1<=n<=45입니다.
 
 입력 : 2     출력 : 2
 입력 : 3     출력 : 3
 
 점화식 이용 가능
 -> 계단 = n, 오르는데 걸리는 걸음 an = an-1 + n - 1
 
 */

#include <iostream>
#include <vector>

using namespace std;

void solution(int input, vector<int> DP){
    cout << DP[input];
}

int main(int argc, const char * argv[]) {
    
    vector<int> DP;
    
    DP.push_back(0);
    DP.push_back(1);
    DP.push_back(2);
    
    for(int i = 3; i<=45; i++){
        int temp = DP[i-1] + i-2;
        DP.push_back(temp);
    }
    
    int input;
    cin >> input;
    
    solution(input, DP);
}
