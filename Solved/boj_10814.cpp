#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[]) {
    int N;
    scanf("%d", &N);
    
    vector<pair<int,pair<int,string>>> user;
        
    for(int i = 0; i < N; i++){
        int age;
        string name;
        cin >> age >> name;
        user.push_back(pair<int,pair<int,string>>(age,make_pair(i,name)));
    }
    
    sort(user.begin(), user.end());
    
    for(int i = 0; i < user.size(); i++){
        cout << user[i].first << " " << user[i].second.second << '\n';
    }
}
