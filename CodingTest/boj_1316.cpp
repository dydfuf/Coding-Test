#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int count;
    
    cin >> count;
    
    int word_count = 0;
    
    for(int i = 0; i < count; i++){
        char word[100];
        int alp[26] = {0};
        cin >> word;
        char temp = word[0];
        int j = 1;
        while(true){
            if(word[j] == '\0'){
                if(alp[word[j-1]-97] > 0){
                    alp[word[j-1]-97]++;
                }
                break;
            }
            if(word[j] != temp){
                alp[temp-97]++;
                temp = word[j];
            }
            j++;
        }
        
        for(int i = 0; i < 27; i++){
            if(i == 26) {
                word_count++;
                break;
            }
            if(alp[i] > 1){
                break;
            }
        }
    }
    cout << word_count << endl;
}
