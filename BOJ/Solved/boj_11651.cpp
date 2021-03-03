#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[]) {
    int N;
    scanf("%d", &N);
    
    vector<pair<int,int>> coor;
    
    for(int i = 0; i < N; i++){
        int x,y;
        scanf("%d %d", &x, &y);
        coor.push_back(pair<int,int>(y,x));
    }
    
    sort(coor.begin(), coor.end());
    
    for(int i = 0; i < coor.size(); i++){
        cout << coor[i].second << " " << coor[i].first << '\n';
    }
}
