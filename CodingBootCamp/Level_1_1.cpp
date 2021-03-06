/*

 Level-1 유효한 회문
 회문은 앞으로, 뒤로 읽어도 같은 글자를 의미합니다.
 문자열을 입력하여 최대 한 문자를 삭제 할 수 있을 때 회문으로 만들 수 있는지 판단 하시오.
 조건 : 문자열의 최대 길이는 50000입니다.
 
 입력 : "aba"     출력 : True
 입력 : "abca"    출력 : True
 
 
 */

#include <iostream>

using namespace std;

bool solution(string input){
    
    for(int i = 0; i < input.size()/2; i++){
        //cout << "front : " << input[i] << " end : " << input[input.size()-1-i] << "\n";
        if(input[i] != input[input.size()-1-i]){
            //cout << "diff!\n";
            for(int j = i; j < input.size()/2; j++){
                //cout << "front++\n";
                //cout << "front : " << input[j+1] << " end : " << input[input.size()-1-j] << "\n";
                if(input[j+1] != input[input.size()-1-j]) return false;
            }
            for(int k = i; k < input.size()/2; k++){
                //cout << "end--\n";
                //cout << "front : " << input[k] << " end : " << input[input.size()-2-k] << "\n";
                if(input[k] != input[input.size()-2-k]) return false;
            }
            return true;
        }
    }
    
    return true;
}

int main(int argc, const char * argv[]) {
    string input;
    
    cin >> input;
            
    
    if(solution(input)) cout << "true";
    else cout << "false";
    
}
