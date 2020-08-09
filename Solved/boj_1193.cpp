/*
|-----|-----|-----|-----|-----|
| 1/1 | 1/2 | 1/3 | 1/4 | 1/5 |
|-----|-----|-----|-----|-----|
| 2/1 | 2/2 | 2/3 | 2/4 | 2/5 |
|-----|-----|-----|-----|-----|
| 3/1 | 3/2 | 3/3 | 3/4 | 3/5 |
|-----|-----|-----|-----|-----|
| 4/1 | 4/2 | 4/3 | 4/4 | 4/5 |
|-----|-----|-----|-----|-----|
| 5/1 | 5/2 | 5/3 | 5/4 | 5/5 |
|-----|-----|-----|-----|-----|
-------------------------------
|-----|-----|-----|-----|-----|
|  1  |  2  |  6  |  7  | 1 5 |
|-----|-----|-----|-----|-----|
|  3  |  5  |  8  | 1 4 |     |
|-----|-----|-----|-----|-----|
|  4  |  9  | 1 3 |     |     |
|-----|-----|-----|-----|-----|
| 1 0 | 1 2 |     |     |     |
|-----|-----|-----|-----|-----|
| 1 1 |     |     |     |     |
|-----|-----|-----|-----|-----|
-------------------------------
시작 :  1 -> 2 -> 4 -> 7 -> 11->
분수 : 1/1->1/2->3/1->1/4->5/1->
방향 : 홀수->우상 , 짝수->좌하
 */

#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {

    int input;
    
    cin >> input;
    
    int level = 0;
    int start = 0;
    
    for(int i = 0; ;i++){
        if(input >= 1 + i*(i-1)/2 && input < 1 + i*(i+1)/2){
            level = i;
            start = 1 + i*(i-1)/2;
            break;
        }
    }
        
    int over = 0, under = 0;
    
    if(level % 2 == 1){
        over = level - (input - start);
        under = 1 + (input - start);
        cout << over << "/" << under;
    }
    else{
        over = 1 + (input - start);
        under = level - (input - start);
        cout << over << "/" << under;
    }
}
