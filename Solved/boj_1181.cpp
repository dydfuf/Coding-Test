#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[]) {
    int N;
    scanf("%d", &N);
    
    vector<pair<int,string>> word;
        
    for(int i = 0; i < N; i++){
        string input;
        cin >> input;
        word.push_back(pair<int,string>(input.length(),input));
    }
    
    sort(word.begin(), word.end());
    word.erase(unique(word.begin(), word.end()), word.end());
    
    for(int i = 0; i < word.size(); i++){
        cout << word[i].second << '\n';
    }
}
