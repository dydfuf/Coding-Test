#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    char word[15];
    cin >> word;
    
    //word to int
    
    int i = 0;
    int sum = 0;
    int word_to_int[15];
    while(true){
        if(word[i] == '\0') break;
        if(word[i] == 'S' || word[i] == 'V' || word[i] == 'Y' || word[i] == 'Z') sum--;
        word_to_int[i] = (word[i] - 65)/3 + 3;
        sum += word_to_int[i];
        i++;
    }
    
    cout << sum;
    
}
