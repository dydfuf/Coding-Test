#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool decs(int a, int b){
    return a > b;
}

int main(int argc, const char * argv[]) {
    int input;
    scanf("%d", &input);
    
    vector<long> vec;
    
    while(input>0){
        vec.push_back(input%10);
        input = input/10;
    }
    
    sort(vec.begin(), vec.end(), decs);
    
    for(int i = 0; i < vec.size(); i++){
        cout << vec[i];
    }
    
}
