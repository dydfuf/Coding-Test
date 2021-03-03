#include <iostream>

using namespace std;

int facto(int n);

int main(int argc, const char * argv[]) {
    
    int input;
   scanf("%d", &input);
    
    if(input == 0) {
        printf("1");
        exit(0);
    }
    else{
        printf("%d", facto(input));
    }
    
}

int facto(int n){
    if(n == 1) return 1;
    return n * facto(n-1);
}
