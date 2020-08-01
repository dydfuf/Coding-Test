#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    
    int a,b;
    
    cin >> a >> b;
    
    int hundred_a,ten_a,one_a;
    int hundred_b,ten_b,one_b;
    
    hundred_a = a/100;
    ten_a = (a - hundred_a*100)/10;
    one_a = (a - hundred_a*100 - ten_a*10);
    
    hundred_b = b/100;
    ten_b = (b - hundred_b*100)/10;
    one_b = (b - hundred_b*100 - ten_b*10);
    
    int first, second, third;
    
    first =  a*one_b;
    second = a*ten_b;
    third = a*hundred_b;
    
    cout << first << endl << second << endl << third << endl << first + second*10 + third*100;
}

