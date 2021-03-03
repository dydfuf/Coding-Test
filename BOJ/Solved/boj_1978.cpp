#include <iostream>

using namespace std;

void Eratos(int n);

bool* PrimeArray = new bool[1001];

int main(int argc, const char * argv[]) {
    
    Eratos(1000);
    
    int count;
    cin >> count;
    
    int ret = 0;
    
    for(int i = 0; i < count; i++){
        int input;
        cin >> input;
        if(PrimeArray[input]) ret++;
    }
    
    cout << ret;
    
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
