#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int a,b,c;
    cin >> a >> b >> c;
    int mul_num = a*b*c;
    int mul_num_one;
    
    int arr[10] = {0};
    
    while(mul_num != 0){
        mul_num_one = mul_num % 10;
        mul_num = mul_num / 10;
        switch (mul_num_one) {
            case 0:
                arr[0]++;
                break;
            case 1:
                arr[1]++;;
                break;
            case 2:
                arr[2]++;;
                break;
            case 3:
                arr[3]++;;
                break;
            case 4:
                arr[4]++;;
                break;
            case 5:
                arr[5]++;;
                break;
            case 6:
                arr[6]++;;
                break;
            case 7:
                arr[7]++;;
                break;
            case 8:
                arr[8]++;;
                break;
            case 9:
                arr[9]++;;
                break;
                
            default:
                break;
        }
    }
    for(int i = 0; i < 10; i++){
        cout << arr[i] << endl;
    }
}
