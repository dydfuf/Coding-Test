#include <iostream>

using namespace std;

int fibo(int n);

int main(int argc, const char * argv[]) {
    
    int input;
    scanf("%d", &input);
    
    printf("%d", fibo(input));
    
}

int fibo(int n){
    if(n <= 1) return n;
    return fibo(n-1) + fibo(n-2);
}
