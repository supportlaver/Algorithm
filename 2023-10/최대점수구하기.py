# dp[i] 의 값을 어떻게 정의할 것 인가?
# i 초 동안 얻을 수 있는 최대 점수

n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(tuple(map(int,input().split())))
dp = [0] * (m+1)
check = [0] * n

for i in range(n):
    check[i] = 1
    t = a[i][1]
    s = a[i][0]
    for j in range(t,m+1):
        dp[j] = max(dp[j] , s+dp[j-t])
print(dp)