import sys
sys.stdin=open("input.txt", "r")
from collections import deque


dx = [0,-1,0,1]
dy = [1,0,-1,0]

m,n= map(int,input().split())

tomato = [list(map(int,input().split())) for _ in range(n)]
dis = [[0]*m for _ in range(n)]
Q = deque()

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            Q.append((i,j))
while Q:
    current = Q.popleft()
    for i in range(4):
        current_x = current[0] + dx[i]
        current_y = current[1] + dy[i]
        if 0<=current_x<n and 0<=current_y<m and tomato[current_x][current_y]==0:
            tomato[current_x][current_y] = 1
            dis[current_x][current_y] += dis[current[0]][current[1]]+1
            Q.append((current_x,current_y))

# 안 익은 토마토가 있는지 확인 flag = 1 이면 모두 익은것이고 , flag = 0 이면 모두 익지 않은 것
flag = 1  
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            flag = 0

result = 0

# 토마토가 모두 익을 때까지의 최소 일 수 를 찾기 위해 dis 의 최대값을 찾는 것
if flag == 1:
    for i in range(n):
        for j in range(m):
            if dis[i][j] > result:
                result = dis[i][j]
    print(result)
else:
    print(-1)






