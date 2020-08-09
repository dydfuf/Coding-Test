//
//  boj_15596.cpp
//  CodingTest
//
//  Created by 최용렬 on 2020/08/02.
//  Copyright © 2020 최용렬. All rights reserved.
//

#include <vector>
long long sum(std::vector<int> &a){
    long long ans = 0;
    for(int i = 0; i < a.size(); i++){
        ans += a[i];
    }
    return ans;
}
