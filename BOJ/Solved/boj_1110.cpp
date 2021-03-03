#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int origin, next, count = 0;
    cin >> origin;
    next = origin;
    while(true){
        int ten = next/10;
        int one = next%10;
        next = one*10 + (ten+one)%10;
        count += 1;
        if(origin == next){
            break;
        }
    }
    cout << count << endl;
}
