//
//  boj_3052.cpp
//  CodingTest
//
//  Created by 최용렬 on 2020/08/01.
//  Copyright © 2020 최용렬. All rights reserved.
//

#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int arr_input[10];
    int divided[42] = {0};
    for(int i = 0; i < 10; i++){
        cin >> arr_input[i];
        divided[arr_input[i]%42]++;
    }
    int sum = 0;
    for(int i = 0; i < 42; i++){
        if(divided[i] != 0) sum++;
    }
    cout << sum;
}

