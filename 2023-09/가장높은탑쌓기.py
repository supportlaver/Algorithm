n = int(input())
box = []
dp = [0] * (n+1)
dp.insert(0,0)

# 밑면의 넓이 , 높이 , 무게
for _ in range(n):
    box.append(list(map(int,input().split())))
box.insert(0,0)

dp[1] = box[1][1]
res = 0

# 조건 1 : 밑면이 좁은 벽돌 위에 밑면이 넓은 벽돌은 놓을 수 없다.
# 조건 2 : 무게가 무거운 벽돌을 무게가 가벼운 벽돌 위에 놓을 수 없다.
for i in range(2,n+1):
    maxx = 0
    for j in range(i-1,0,-1):
        if box[j][0] > box[i][0] and box[j][2] > box[i][2] and maxx < dp[j]:
            maxx = dp[j]
    dp[i] = maxx + box[i][1]
    if res < dp[i]:
        res = dp[i]
print(dp)

