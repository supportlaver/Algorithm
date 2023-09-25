n = int(input())
# 돌다리의 개수만 보는 것이 아니라 마지막에 건너편까지 가는 경우의 수 까지 생각해야 한다.
# 그래서 dp[n] 을 구하는 것이 아닌 dp[n+1] 을 구해야 한다.
dp = [0] * (n+2)
dp[1] = 1
dp[2] = 2
for i in range(3,n+2):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n+1])


