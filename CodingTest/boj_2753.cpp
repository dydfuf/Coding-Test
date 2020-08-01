#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int year;
    
    cin >> year;
    
    bool four = false, hundred = false, four_hundred = false;
    
    if(year % 4 == 0){
        four = true;
    }
    
    if(year % 100 == 0){
        hundred = true;
    }
    
    if(year % 400 == 0){
        four_hundred = true;
    }
    
    if((four && !hundred) || four_hundred){
        cout << "1";
    }
    else cout << "0";
}
