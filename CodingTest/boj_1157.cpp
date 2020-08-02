#include <iostream>
#include <string>

using namespace std;

int main(int argc, const char * argv[]) {
    
    // 아스키 'A' : 65 ~ 'Z' : 90, 'a' : 97 ~ 'z' : 122
    
    char word[1000000];
    int ascii[26] ={0};
    int i = 0;
    
    cin >> word;
    
    while(true){
        if(word[i] == '\0') break;
        
        if(word[i] >= 'A' && word[i] <= 'Z'){
            ascii[word[i]-65]++;
        }
        else if(word[i] >= 'a' && word[i] <= 'z'){
            ascii[word[i] - 97]++;
        }
        i++;
    }
    
    int result = ascii[0];
    int idx = 0;
    
    for(int i = 0; i < 26; i++){
        if(result < ascii[i]){
            result = ascii[i];
            idx = i;
        }
    }
    
    int count = 0;
    
    for(int i = 0; i < 26; i++){
        if(ascii[i] == result) count++;
    }
    
    if(count > 1){
        cout << "?" << endl;
        exit(0);
    }
    
    char a = idx+65;
    
    cout << a << endl;

}
