#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;


    for(int i=3; i < 5000; i++){
        for(int j = i; j< 5000; j++){
            if((brown+yellow) == i*j && (i-2)*(j-2) == yellow){
                answer.push_back(j);
                answer.push_back(i);
                return answer;
            }
        }
    }
    return answer;
}