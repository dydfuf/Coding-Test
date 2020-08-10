#include <iostream>

using namespace std;

void Eratos(int n);

bool* PrimeArray = new bool[10001];

int main(int argc, const char * argv[]) {
    
    Eratos(10000);
    
    int M,N;
    cin >> M >> N;
    
    int Min = -1;
    int sum = 0;
    
    for(int i = M; i <= N; i++){
        if(PrimeArray[i]){
            sum += i;
        }
    }
    
    for(int i = M; i <= N; i++){
        if(PrimeArray[i]){
            Min = i;
            break;
        }
    }
    if(Min == -1) cout << "-1";
    else cout << sum << endl << Min;
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
