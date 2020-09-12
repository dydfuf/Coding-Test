/*

 Level-3 고인 물의 양 계산하기
 
 위와같은 지형을 배열로 나타내면
 [0,1,0,2,1,0,1,3,2,1,2,1]이 됩니다.
 비가 왔을 때 저 검은색 지형에 담 길 수 있는 물의 양을 구하시오
 
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solution(){
    
    //vector<int> a = {0,1,0,2,1,0,1,3,2,1,2,1};
    vector<int> a = {0,2,0,2,0,1,1,3,1,1,2,0};
    
    vector<int> temp_front(a.size());
    vector<int> temp_back(a.size());
    vector<int> ans(a.size());
    
    
    for(int i = 0, max = 0; i < a.size(); i++){
        if(a[i]>max) max = a[i];
        if(max>a[i]) temp_front[i] = max;
    }
    
    for(int i = 0, max = 0; i < a.size(); i++){
        if(a[a.size()-i-1]>max) max = a[a.size()-i-1];
        if(max>a[a.size()-i-1]) temp_back[a.size()-i-1] = max;
    }
    for(int i = 0; i < a.size(); i++){
        
        int water_top = min(temp_front[i],temp_back[i]);
        
        if(water_top>0) ans[i] = water_top-a[i];
        else ans[i] = water_top;
    }
    
    
    for(auto i : temp_front) cout << i;
    cout << endl;
    for(auto i : temp_back) cout << i;
    cout << endl;
    int sum = 0;
    for(auto i : ans){
        cout << i;
        sum += i;
    }
    cout << endl << sum;
}

int main(int argc, const char * argv[]) {
    solution();
}
