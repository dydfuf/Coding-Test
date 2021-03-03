#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    
    char word[1000000];
    
    cin.getline(word, 1000000); // 공백포함 입력 받기
    
    int i = 0;
    int count = 0;
    
    if(word[0] == ' ') count--;
    
    while(true){
        if(word[i] == '\0'){
            if(word[i-1] == ' ') count--;
            break;
        }
        if(word[i] == ' ' ) count++;
        i++;
    }

    cout << count+1 << endl;

}
