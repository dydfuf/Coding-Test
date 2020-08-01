#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int x;
    
    cin >> x;
    
    for(int i = 0; i < x; i++){
        cout << x - i << '\n';
    }
}

// 시간 초과가 계속 났음.
// endl 을 '\n'으로 바꾸니 시간초과 안남.
// endl은 단순 개행뿐만 아니라 출력버퍼를 지워주는 역할도 함 따라서 시간이 오래 걸림.
