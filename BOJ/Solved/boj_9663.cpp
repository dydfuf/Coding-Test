#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
bool chess[16][16];
int queen_count = 0;

bool isValid(int x, int y){
    
    for(int i = 1; i <= N; i++){
        if(chess[x][i] == false || chess[i][y] == false) return false;
    }
    
    int diag = 1;
    
    while(x+diag<=N && y+diag<=N){
        if(chess[x+diag][y+diag] == false) return false;
        diag++;
    }
    diag = 1;
    
    while(x-diag>0 && y-diag>0){
        if(chess[x-diag][y-diag] == false) return false;
        diag++;
    }
    diag = 1;
    
    while(x+diag<=N && y-diag>0){
        if(chess[x+diag][y-diag] == false) return false;
        diag++;
    }
    diag = 1;
    
    while(x-diag>0 && y+diag<=N){
        if(chess[x-diag][y+diag] == false) return false;
        diag++;
        
    }
    
    return true;
    
}

void put(int input){

    if(input == N+1){
        queen_count++;
        return;
    }
    
    
    for(int i = 1; i <= N; i++){
        if(chess[i][input] && isValid(i, input)){
            chess[i][input] = false;
            put(input+1);
            chess[i][input] = true;
        }
    }
    
}

void init(void){
    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= N; j++){
            chess[i][j] = true;
        }
    }
}

int main(int argc, const char * argv[]) {
    scanf("%d", &N);
    init();
    
    put(1);
    cout << queen_count;
}


