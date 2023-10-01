# dp[i] 의 값을 어떻게 정의할것인가?
# i 를 거슬러 줄 수 있는 동전의 최소 개수
# 가방 문제 처럼 동전 한 개만 있다고 가정을 하면서 문제를 풀기 시작

n = int(input())
coins = list(map(int,input().split()))
m = int(input())
dp = [1000] * (m+1)
for i in range(n):
    current_coin = coins[i]
    for j in range(current_coin,m+1):
        if j % current_coin == 0:
            dp[j] = min(dp[j],j//current_coin)
        else:
            dp[j] = min(dp[j],j//current_coin + dp[j%current_coin])
print(dp[m])

# 또 다른 풀이
my_dp = [1000] * (m+1)
my_dp[0] = 0
for i in range(n):
    for j in range(coins[i],m+1):
        # coins[i] 로 들어온 것 만큼의 동전 1개와 그 나머지는 my_dp[j-coins[i]] 에 있다.
        # 그래서 1+ my_dp[j-coins[i]] 와 비교
        my_dp[j] = min(my_dp[j] , my_dp[j-coins[i]] + 1)
print(my_dp[m])
