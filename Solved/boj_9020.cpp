/*
 시간을 줄이는 것이 포인트!
 */

#include <iostream>

using namespace std;

void Eratos(int n);

bool* PrimeArray = new bool[10001];

int main(int argc, const char * argv[]) {
    
    Eratos(10000);
    
    int count;
    cin >> count;
    
    for(int i = 0; i < count; i++){
        int input;
        cin >> input;
        
        int temp1 = 0, temp2 = 0;
                
        for(int i = input/2; i <= input; i++){
            if(PrimeArray[i]){
                temp1 = i;
                for(int j = input/2; j > 0; j--){
                    if(PrimeArray[j]){
                        temp2 = j;
                        if(temp1 + temp2 == input){
                            cout << temp2 << " " << temp1 << '\n';
                            j = 0;
                            i = input+1;
                        }
                    }
                }
            }
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


