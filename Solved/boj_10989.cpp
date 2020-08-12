#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    
    int N;
    scanf("%d", &N);

    int arr[10001] = {0};
    
    for(int i = 0; i < N; i++){
        int input;
        scanf("%d", &input);
        arr[input]++;
    }
    
    for(int i = 1; i <= 10000; i++){
        for(int j = 0; j < arr[i]; j++){
            printf("%d\n", i);
        }
    }
}
