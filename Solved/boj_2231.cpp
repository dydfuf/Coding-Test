#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    
    int input;
    cin>>input;
    
    for(int i = 0; i < 1000000; i++){
        int temp = i;
        int ans = temp;
        
        while(temp>0){
            ans += temp%10;
            temp = temp/10;
        }
        if(ans == input){
            cout << i;
            exit(0);
        }
    }
    cout << "0";
    
}
