#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[]) {
    int N;
    scanf("%d", &N);
    
    vector<int> arr;
    
    for(int i = 0; i < N; i++){
        int input;
        scanf("%d", &input);
        arr.push_back(input);
    }
    
    sort(arr.begin(), arr.end());
    
    for(int i = 0; i < arr.size(); i++){
        printf("%d\n", arr[i]);
    }
}
