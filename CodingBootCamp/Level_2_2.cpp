/*

 Level-2 일정간격의 병합
 
 입력 : [[1,3], [2,6], [8,10], [15,18]]
 출력 : [[1,6], [8,10], [15,18]
 
 위와같이 아무 규칙도 없는 간격의 모음 들이 입력 되면 겹치는 간격을 병합합니다.
 
 입력 : [[1,4], [4,5]]            출력 : [[1,5]]
 입력 : [[1,9], [2,6], [16,25]]   출력 : [[1,9], [16,26]]
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<pair<int,int>> input;
vector<pair<int,int>> output;

void init(){
    
    /*
    input.push_back(pair<int,int>(1,3));
    input.push_back(pair<int,int>(2,6));
    input.push_back(pair<int,int>(8,10));
    input.push_back(pair<int,int>(15,18));
     */
    
    /*
    input.push_back(pair<int,int>(1,4));
    input.push_back(pair<int,int>(4,5));
     */
    
    input.push_back(pair<int,int>(1,9));
    input.push_back(pair<int,int>(2,6));
    input.push_back(pair<int,int>(16,25));
    
}

void solution(){
    
    init();
    
    sort(input.begin(), input.end());
    
    int start = input[0].first;
    int end = input[0].second;
    
    for(int i = 1; i < input.size(); i++){
        
        if(input[i].first <= end){
            end = input[i].second;
        }
        else{
            start = input[i].first;
            end = input[i].second;
        }
        output.push_back(pair<int,int>(start,end));
    }
    
    for(int i = 0; i < output.size(); i++){
        cout << output[i].first << " " << output[i].second << "\n";
    }

}

int main(int argc, const char * argv[]) {
    solution();
}
