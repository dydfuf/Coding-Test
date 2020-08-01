#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[]) {
    int num;
    vector<int> arr;
    cin >> num;
    
    for(int i = 0; i < num; i++){
        int input;
        cin >> input;
        arr.push_back(input);
    }
    sort(arr.begin(), arr.end());
    cout << arr.front() << endl << arr.back();
}
