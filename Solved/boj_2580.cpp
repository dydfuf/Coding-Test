#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

int sudoku[10][10] = {0,};
bool able[10][10][10];
vector<pair<int,int>> fill_list;
int to_fill = 0;

void find_able(int x, int y){
    
    //가로세로
    for(int i = 0; i < 10; i++){
        int temp = sudoku[x][i];
        able[x][y][temp] = false;
        temp = sudoku[i][y];
        able[x][y][temp] = false;
    }
    
    //작은 정사각형
    if((x >= 0 && x <= 2) && (y >= 0 && y <= 2)){
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                int temp = sudoku[i][j];
                able[i][j][temp] = false;
            }
        }
    }
    else if((x >= 0 && x <= 2) && (y >= 3 && y <= 5)){
        for(int i = 0; i < 3; i++){
            for(int j = 3; j < 6; j++){
                int temp = sudoku[i][j];
                able[i][j][temp] = false;
            }
        }
    }
    else if((x >= 0 && x <= 2) && (y >= 6 && y <= 8)){
        for(int i = 0; i < 3; i++){
            for(int j = 6; j < 9; j++){
                int temp = sudoku[i][j];
                able[i][j][temp] = false;
            }
        }
        
    }
    
    else if((x >= 3 && x <= 5) && (y >= 0 && y <= 2)){
        for(int i = 3; i < 6; i++){
            for(int j = 0; j < 3; j++){
                int temp = sudoku[i][j];
                able[i][j][temp] = false;
            }
        }
        
    }
    else if((x >= 3 && x <= 5) && (y >= 3 && y <= 5)){
        for(int i = 3; i < 6; i++){
            for(int j = 3; j < 6; j++){
                int temp = sudoku[i][j];
                able[i][j][temp] = false;
            }
        }
        
    }
    else if((x >= 3 && x <= 5) && (y >= 6 && y <= 8)){
        for(int i = 3; i < 6; i++){
            for(int j = 6; j < 9; j++){
                int temp = sudoku[i][j];
                able[i][j][temp] = false;
            }
        }
        
    }
    
    else if((x >= 6 && x <= 8) && (y >= 0 && y <= 2)){
        for(int i = 6; i < 9; i++){
            for(int j = 0; j < 3; j++){
                int temp = sudoku[i][j];
                able[i][j][temp] = false;
            }
        }
        
    }
    else if((x >= 6 && x <= 8) && (y >= 3 && y <= 5)){
        for(int i = 6; i < 9; i++){
            for(int j = 3; j < 6; j++){
                int temp = sudoku[i][j];
                able[i][j][temp] = false;
            }
        }
        
    }
    else if((x >= 6 && x <= 8) && (y >= 6 && y <= 8)){
        for(int i = 6; i < 9; i++){
            for(int j = 6; j < 9; j++){
                int temp = sudoku[i][j];
                able[i][j][temp] = false;
            }
        }
        
    }
    
}

void find_num(int M){
    
    if(M == fill_list.size()){
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                printf("%d ", sudoku[i][j]);
            }
            printf("\n");
        }
        exit(0);
        return;
    }
    
    for(int i = 1; i <= 9; i++){
        if(able[fill_list[M].first][fill_list[M].second][i]){
            able[fill_list[M].first][fill_list[M].second][i] = false;
            sudoku[fill_list[M].first][fill_list[M].second] = i;
            find_num(M+1);
            sudoku[fill_list[M].first][fill_list[M].second] = 0;
            able[fill_list[M].first][fill_list[M].second][i] = true;
        }
    }
    
}

void init(void){
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            for(int k = 0; k < 10; k++){
                able[i][j][k] = true;
            }
        }
    }
    
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            scanf("%d", &sudoku[i][j]);
        }
    }
    
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            if(sudoku[i][j] == 0){
                fill_list.push_back(pair<int,int>(i, j));
                to_fill++;
                find_able(i, j);
            }
        }
    }
}

int main(int argc, const char * argv[]) {
    
    init();

    
    find_num(0);
    
}


