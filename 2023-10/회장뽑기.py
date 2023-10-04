n = int(input())
dis = [[100]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    dis[i][i] = 0

info = []

while True:
    s,e = map(int,input().split())
    if s==-1 and e==-1:
        break
    # 무방향 그래프이기 떄문에 양쪽에 가중치를 부여
    dis[s][e] = 1
    dis[e][s] = 1

# 플로이드 워샬 알고리즘
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dis[i][j] = min(dis[i][j] , dis[i][k]+dis[k][j])

# 정답 출력 방법 1
res = [1000] * (n+1)
for i in range(1,n+1):
    maxx = -2147000
    for j in range(1,n+1):
        if dis[i][j] > maxx:
            maxx = dis[i][j]
    res[i] = maxx

minn = min(res)
cnt = 0
for r in res:
    if minn == r:
        cnt+=1
print(minn , cnt)
for i in range(1,n+1):
    if res[i] == minn:
        print(i,end= " ")


# 정답 출력 방법 2
my_res = [0] * (n+1)
score = 100;
for i in range(1,n+1):
    for j in range(1,n+1):
        res[i] = max(res[i] , dis[i][j])
    score = min(score,res[i])

out = []
for i in range(1,n+1):
    if res[i] == score:
        out.append(i)
print("%d %d" %(score,len(out)))

for o in out:
    print(o, end=" ")