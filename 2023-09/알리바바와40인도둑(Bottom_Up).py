n = int(input())
rock = [list(map(int,input().split())) for _ in range(n)]

# (0,0) 부터 (n-1,n-1) 까지 가는데 드는 최소 에너지 출력

# dp[i][j] 는 (0,0) 에서 부터 (i,j) 까지 가는데 드는 최소 에너지를 넣는다.

# dp[0][j] , dp[i][0] 은 올 수 있는 곳들이 정해져있기 때문에 미리 초기화를 시켜놓고 시작한다.
# 최단 거리 이동을 하기 때문에 특정 한 곳에서 올 수 있는 부분은 위에서 오거나 왼쪽에서 오는 경우만 있다.
# 그래서 왼쪽에 올 때와 , 위에서 올때 중 최소 값을 가지고 해당 에너지를 더해가면서 dp 를 채워나간다.

dp = [[0]*n for _ in range(n)]

dp[0][0] = rock[0][0]

# dp 초기화
for i in range(1,n):
    dp[i][0] = dp[i-1][0] + rock[i][0]
    dp[0][i] = dp[0][i-1] + rock[0][i]

for i in range(1,n):
    for j in range(1,n):
        # 위에서 올떄와 왼쪽에서 올때를 비교하고 가장 작은 값에 해당 에너지를 더해준것을 dp 에 넣어준다.
        minn = min(dp[i-1][j] , dp[i][j-1])
        dp[i][j] = minn + rock[i][j]
print(dp[n-1][n-1])
