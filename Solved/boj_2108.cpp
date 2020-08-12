#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool desc(int a, int b){
    return a > b;
}

int main(int argc, const char * argv[]) {
    int N;
    scanf("%d", &N);
    
    vector<int> arr1,arr2;
    int arr3[8001] = {0};
    
    for(int i = 0; i < N; i++){
        int input;
        scanf("%d", &input);
        arr1.push_back(input);
        arr2.push_back(input);
        arr3[input+4000]++;
    }
    
    sort(arr2.begin(), arr2.end(), desc);
    
    double sum = 0;
    int temp = arr3[0], idx = 0;
    double one, two, three, four;
    
    for(int i = 0; i < arr1.size(); i++){
        sum += arr1[i];
    }
        
    for(int i = 0; i < 8001; i++){
        if(temp < arr3[i]) {
            temp = arr3[i];
            idx = i;
        }
    }
    
    vector<double> most;

    for(int i = 0; i < 8001; i++){
        if(arr3[i] == temp) most.push_back(i);
    }
    
    one = sum/N;
    if(most.size() == 1) three = idx-4000;
    else three = most[1]-4000;
    two = arr2[(N-1)/2];
    four = arr2.front()-arr2.back();

    
    printf("%.0lf\n%.0lf\n%.0lf\n%.0lf\n", one, two, three, four);
    
}
