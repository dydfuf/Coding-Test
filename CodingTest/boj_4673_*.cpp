#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int d(int input);

vector<int> v;

int main(int argc, const char * argv[]) {
    
    // d의 인자를 0부터 10000까지
    for(int i = 1; i < 10000; i++){
        d(i);
    }
    
    //정렬후 중복값 삭제
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(),v.end()),v.end());
    
    //벡터 v는 우리가 원하는 수열의 반대임 filp하기 위함
    int bool_arr[10000] = {0};
    
    for(int i = 0; i < v.size(); i++){
        if(v[i] > 10000) break;
        bool_arr[v[i]] = 1;
    }
    
    //flip된 값 출력
    for(int i = 0; i < 10000; i++){
        if(bool_arr[i] == 0) cout << i << endl;
    }
}

int d(int input){
    if(input > 10000) return 0;
    int ret = 0;
    ret += input;
    while(input>0){
        ret += input%10;
        input = input/10;
    }
    v.push_back(ret);
    return d(ret);
}

------------------------------------------------------

