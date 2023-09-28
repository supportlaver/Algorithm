# 밑면의 넓이를 내림차순으로 먼저 정렬을 시켜놓자.
# 그러면 무게의 조건만 만족하면 된다.

# dp 에 들어가는 값은 해당 인덱스의 box 가 가장 꼭대기에 있을 때의 최대 높이를 넣는다.
# dp[4] 는 4번째 벽돌을 맨 꼭대기에 놓았을 때 탑의 최대 높이를 넣어주면 되다는 것이다.

n = int(input())
box = []
for i in range(n):
    # 밑면의 넓이 , 높이 , 무게
    a,b,c = map(int,input().split())
    box.append((a,b,c))

# 밑면의 넓이를 기준으로 내림차순으로 정렬 (0번 인덱스로 정렬된다.) 
box.sort(reverse=True)
box.insert(0,0)

dp = [0] * (n+1)
dp.insert(0,0)

dp[1] = box[1][1]
res = box[1][1]

for i in range(2,n+1):
    maxx = 0
    for j in range(i-1,0,-1):
        if box[j][2] > box[i][2] and dp[j]>maxx:
            maxx = dp[j]
    dp[i] = maxx + box[i][1]
    if res < dp[i]:
        res = dp[i]
print(res)

