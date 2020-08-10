#include <iostream>

using namespace std;

void Eratos(int n);

bool* PrimeArray = new bool[1000001];

int main(int argc, const char * argv[]) {
    
    Eratos(1000000);
    
    int M,N;
    cin >> M >> N;
 
    
    for(int i = M; i <= N; i++){
        if(PrimeArray[i]){
            cout << i << '\n';
        }
    }
}

void Eratos(int n){
    
    for(int i = 2; i <=n; i++){
        PrimeArray[i] = true;
    }
    
    for(int i = 2; i * i <= n; i++){
        if(PrimeArray[i]){
            for(int j = i*i; j <= n; j+=i){
                PrimeArray[j] = false;
            }
        }
    }
}
