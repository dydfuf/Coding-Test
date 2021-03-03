#include <iostream>

using namespace std;

void Eratos(int n);

bool* PrimeArray = new bool[246913];

int main(int argc, const char * argv[]) {
    
    Eratos(246912);
    
    while(true){
        int n;
        cin >> n;
        if(n == 0) break;
        int sum = 0;
        
        if(n == 1){
            cout << "1" << '\n';
        }
        else{
            for(int j = n+1; j <= 2*n; j++){
                if(PrimeArray[j]){
                    sum++;
                }
            }
            cout << sum << '\n';
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
