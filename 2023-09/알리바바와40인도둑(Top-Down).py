
def DFS(x,y):
    if dp[x][y] != 0:
        return dp[x][y]
    # 가장자리에 있을때는 올 수 있는 곳이 한정되기 떄문에 따로 분기문으로 걸러줘야한다.
    elif x==0:
        dp[x][y] = DFS(x,y-1) + rock[x][y]
        return dp[x][y]
    elif y==0:
        dp[x][y] = DFS(x-1,y) + rock[x][y]
        return dp[x][y]
    else:
        dp[x][y] = min(DFS(x-1,y), DFS(x,y-1)) + rock[x][y]
        return dp[x][y]

if __name__=="__main__":
    n = int(input())
    rock = [list(map(int,input().split())) for _ in range(n)]
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = rock[0][0]
    # dp 초기화
    for i in range(1,n):
        dp[i][0] = dp[i-1][0] + rock[i][0]
        dp[0][i] = dp[0][i-1] + rock[0][i]
    print(DFS(n-1,n-1))
