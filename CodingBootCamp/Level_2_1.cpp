/*

 Level-2 섬의 갯수
 
 [1,1,1,1,0],
 [1,1,0,1,0],
 [1,1,0,0,0],
 [0,0,0,0,0]
 
 이러한 배열이 있을 때 1을 제외 하고는 모두 바다입니다.
 이때 섬의 개수를 찾으십시오,(단 괄호는 모두 바다로 생각해도 좋습니다.
 
 위 예제는 섬이 하나입니다.
 
 
 */

#include <iostream>

using namespace std;

#define width 5
#define height 4

/*
int graph[height][width] = {
    {1,1,1,1,0},
    {1,1,0,1,1},
    {1,1,0,0,0},
    {0,0,0,0,0}
};
*/

/*
int graph[height][width] = {
    {1,1,0,0,0},
    {1,1,0,0,0},
    {0,0,1,0,0},
    {0,0,0,1,1}
};
*/

int graph[height][width] = {
    {1,1,0,1,0},
    {1,1,0,0,1},
    {0,0,1,0,0},
    {1,1,0,1,1}
};

bool visited[height][width];

// 우 하 좌 상
int dw[4] = {1,0,-1,0};
int dh[4] = {0,1,0,-1};

int land = 0;

void dfs(int h, int w){
    visited[h][w] = true;
    
    for(int i = 0; i < 4; i++){
        int new_h = h + dh[i];
        int new_w = w + dw[i];
        
        if(0 <= new_w && 0 <= new_h && new_w < width && new_h < height){
            if(graph[new_h][new_w] && !visited[new_h][new_w]){
                visited[new_h][new_w] = true;
                dfs(new_h, new_w);
            }
        }
    }
}

void solution(){
    
    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            if(graph[i][j] && !visited[i][j]){
                land++;
                dfs(i,j);
            }
        }
    }
    cout << land;
}

int main(int argc, const char * argv[]) {
    solution();
}
