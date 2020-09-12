/*

 Level-3 정렬 된 두 배열의 중앙값
 
 두 개의 정렬 된 배열을 모두 살펴보고 중간 값을 반환하시오
 단 런타임은 O(log(m+n))을 초과하면 안됩니다.
 
 Num1.length = m
 Num2.length = n
 0 <= m, n <= 1000
 -10^6 <= num1[i],num2[i] <= 10^6
 
 https://stackoverrun.com/ko/q/12165944
 
 */

#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

#define MAX_VALUE 9999999

double getkth(vector<int> A, int aStart, vector<int> B, int bStart, int k){
    if(aStart > (int)A.size() - 1 ) return B[bStart + k -1];
    if(bStart > (int)B.size() - 1 ) return A[aStart + k -1];
    if( k == 1) return min(A[aStart],B[bStart]);
    
    int aMid = MAX_VALUE, bMid = MAX_VALUE;
    
    if(aStart + k/2 -1 < (int)A.size() ) aMid = A[aStart + k/2 -1];
    if(bStart + k/2 -1 < (int)B.size() ) bMid = B[bStart + k/2 -1];
    
    if( aMid < bMid)
        return getkth(A, aStart + k/2, B, bStart, k - k/2);
    else
        return getkth(A, aStart, B, bStart + k/2, k - k/2);
    
}

double solution(vector<int> A, vector<int> B){
    int m = (int)A.size(), n = (int)B.size();
    
    int l = (m + n + 1)/2;
    int r = (m + n + 2)/2;
    return (getkth(A, 0, B, 0, l) + getkth(A, 0, B, 0, r)) / 2;
}

int main(int argc, const char * argv[]) {
    vector<int> A = {1,2,100};
    vector<int> B = {4,5,6};
    
    cout << solution(A,B);
}
