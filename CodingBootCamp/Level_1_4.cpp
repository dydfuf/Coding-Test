/*

 Level-4 반전 이진 트리
 
 트리를 오른쪽 처럼 반전 시키시오
 
 입력 : [4,2,7,1,3,6,9]
 출력 : [4,7,2,9,6,3,1]
 
 */

#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

void solution(vector<int> tree){
    vector<int> temp;
    temp.push_back(tree[0]);
    
    int count = 2;
    int begin = 1;
    int end = 2;
    
    while(true){
        
        for(int i = end; i >= begin; i--){
            temp.push_back(tree[i]);
        }
        
        begin = end + 1;
        end = end + count*2;
        count *= 2;
        
        if(end > tree.size()) break;
    }
    
    for(int i = 0; i < temp.size(); i++){
        cout << temp[i] << " ";
    }
}

int main(int argc, const char * argv[]) {
    
    vector<int> tree = {4,2,7,1,3,6,9};
    
    solution(tree);
}
