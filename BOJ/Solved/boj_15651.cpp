#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int M,N;
int arr[9];
bool visitied[9];

void func(int cnt){
    
    if(cnt == M){
        vector<int> vec;
        for(int i = 0; i < M; i++){
            cout << arr[i] << " ";
        }
        cout << '\n';
        return;
    }
    
    for(int i = 1; i <= N; i++){
        arr[cnt] = i;
        func(cnt+1);
    }
    
}

int main(int argc, const char * argv[]) {
    scanf("%d %d", &N, &M);
    func(0);
    return 0;
    
}
