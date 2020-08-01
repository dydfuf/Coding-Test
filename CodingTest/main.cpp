//
//  main.cpp
//  CodingTest
//
//  Created by 최용렬 on 2020/07/01.
//  Copyright © 2020 최용렬. All rights reserved.
//

#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int count;
    int x = 0, sum = 0;
    cin >> count;
    for(int i = 0; i < count; i++){
        char c_arr[80];
        cin >> c_arr;
        for(int j = 0; j < 80; j++){
            if(c_arr[j] == '\0') break;
            
            if(c_arr[j] == 'O'){
                x++;
                sum += x;
            }
            else{
                x = 0;
            }
        }
        cout << sum << endl;
        sum = 0;
        x = 0;
    }
}
