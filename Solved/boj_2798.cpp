#include <iostream>
#include <vector>

using namespace std;

int main(int argc, const char * argv[]) {
    int M,N;
    
    cin >> N >> M;
    
    vector<int> card;
    
    for(int i = 0; i < N; i++){
        int input;
        cin >> input;
        card.push_back(input);
    }
    
    vector<int> sum, diff;
    
    for(int i = 0; i < N; i++){
        for(int j = i+1; j < N; j++){
            for(int k = j+1; k < N; k++){
                sum.push_back(card[i]+card[j]+card[k]);
                diff.push_back(M-(card[i]+card[j]+card[k]));
            }
        }
    }

    int ans = M, idx = 0;
    
    for(int i = 0; i < sum.size(); i++){
        int temp = diff[i];
        if(temp >= 0){
            if(temp < ans){
                ans = temp;
                idx = i;
            }
        }
    }
    
    cout << sum[idx];
}
