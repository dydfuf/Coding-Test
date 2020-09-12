/*

 Level-2 단어 나누기
 
 띄어쓰기가 없는 문자열에 단어의 기준을 정해주고 띄어쓰기를 만들어 주시오
 
 입력 : "applepenapple",["apple","pen"]
 출력 : true
 
 입력 : "caukkcaukcau", ["cau","k"]
 출력 : true
 */

#include <iostream>
#include <vector>

using namespace std;

vector<int> getPi(string p){
    int m = (int)p.size(), j = 0;
    vector<int> pi(m);
    for(int i = 1; i < m; i++){
        while(j > 0 && p[i] != p[j]){
            j = pi[j-1];
        }
        if(p[i] == p[j]){
            pi[i] = ++j;
        }
    }
    return pi;
}

vector<int> kmp(string s, string p){
    vector<int> ans;
    vector<int> pi = getPi(p);
    int n = (int)s.size(), m = (int)p.size(), j = 0;
    for(int i = 0; i < n; i++){
        while(j > 0 && s[i] != p[j]){
            j = pi[j-1];
        }
        if(s[i] == p[j]){
            if(j == m-1){
                ans.push_back(i-m+1);
                j = pi[j];
            }
            else j++;
        }
    }
    return ans;
}

bool solution(){
    string input = "applepenapple";
    vector<string> set = {"apple", "pen"};
    
    for(int i = 0; i < set.size(); i++){
        vector<int> match = kmp(input, set[i]);
        
        if(match.size() == 0) return false;
        
    }
    return true;
}

int main(int argc, const char * argv[]) {

    if(solution()) cout << "true";
    else cout << "false";
}
