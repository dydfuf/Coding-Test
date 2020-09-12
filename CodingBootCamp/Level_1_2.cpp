/*

 Level-2 0이동
 
 배열이 주어지면 0을 맨 뒤로 정렬하고 다른 수는 순서를 유지해야 합니다.
 
 조건 : 배열, 튜플 등 복사본을 만들지 않고 수행 하십시오
 
 입력 : [0,1,0,4,3,12]
 출력 : [1,4,3,12,0,0]
 
 */

#include <iostream>
#include <vector>

using namespace std;

void solution(vector<int> arr){
    
    int count = 0;
    
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] == 0) count++;
        else cout << arr[i] << " ";
    }
    
    for(int i = 0; i < count; i++){
        cout << "0 ";
    }
}

int main(int argc, const char * argv[]) {
    
    vector<int> arr = {0,1,0,4,3,12};
    
    solution(arr);
}
