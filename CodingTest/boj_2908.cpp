#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    
    int a,b;
    
    cin >> a >> b;
    
    int hundred_a, ten_a, one_a;
    int hundred_b, ten_b, one_b;
    
    hundred_a = a/100;
    ten_a = (a-hundred_a*100)/10;
    one_a = (a-hundred_a*100-ten_a*10);
    
    hundred_b = b/100;
    ten_b = (b-hundred_b*100)/10;
    one_b = (b-hundred_b*100-ten_b*10);
    
    int new_a, new_b;
    
    new_a = one_a*100 + ten_a*10 + hundred_a;
    new_b = one_b*100 + ten_b*10 + hundred_b;
        
    if(new_a > new_b) cout << new_a;
    else cout << new_b;
}
