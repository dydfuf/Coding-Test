#include <cstdio>
using namespace std;

int dx[4] = { 1, 0, -1, 0};
int dy[4] = { 0, 1, 0, -1};
int arr[501][501];
int dp[501][501];
int n, m;

int dfs(int y, int x) {
    int k;

    if (y == m && x == n) {
        return 1;
    }
    else if (dp[y][x] == -1) {
        dp[y][x] = 0;
        for (k = 0; k < 4; k++) {
            int newy = y + dy[k];
            int newx = x + dx[k];
            if (newx > 0 && newx <= n && newy > 0 && newy <= m && arr[y][x] > arr[newy][newx]) {
                dp[y][x] += dfs(newy, newx);
            }
        }
    }
    return dp[y][x];
}

int main() {

    scanf("%d %d", &m, &n);

    int i, j;

    for (i = 0; i <= m; i++) {
        for (j = 0; j <= n; j++)  {
            dp[i][j] = -1;
            arr[i][j] = 10001;
        }
    }

    for (i = 1; i <= m; i++) {
        for (j = 1; j <= n; j++) {
            scanf("%d", &arr[i][j]);
        }
    }

    printf("%d\n", dfs(1,1));

    return 0;
}
