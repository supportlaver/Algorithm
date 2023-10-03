# 플로이드 워샬 알고리즘이란 ?
# 모든 정점에서 모든 정점으로 가는 알고리즘 -> 1번 정점에서 또 다른 정점으로 가는 최단 거리를 구하는 것
# 그렇다면 dp 리스트는 2차원이 될 것 이다. (전에 했었던 냅색 알고리즘이란 유사)
# 여기서는 dp 테이블을 dis 라고 하자.
# dis[i][j] 와 dis[i][k] + dis[k][j] 중에서 최소 값을 찾으면서 갱신해나가자 

n,m=map(int,input().split())

roads = [list(map(int,input().split())) for _ in range(m)]

dis = [[1000]*(n+1) for _ in range(n+1)]

for i in range(m):
    s = roads[i][0]
    e = roads[i][1]
    v = roads[i][2]
    dis[s][e] = v

for i in range(1,n+1):
    dis[i][i] = 0

# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             dis[i][j] = min(dis[i][j] , dis[i][k]+dis[k][j])

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dis[i][j] = min(dis[i][j] , dis[i][k]+dis[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if dis[i][j] == 1000:
            print("M",end=" ")
        else:
            print(dis[i][j],end=" ")
    print()