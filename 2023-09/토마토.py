import sys
from collections import deque
sys.stdin = open("input.txt" , "r")
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n , m = map(int,input().split())
tomato = [list(map(int,input().split()))for _ in range(m)]

Q = deque()
dis = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            Q.append((i,j))

while Q:
    current = Q.popleft()
    for i in range(4):
        current_x = current[0] + dx[i]
        current_y = current[1] + dy[i]
        if 0<=current_x<m and 0<=current_y<n and tomato[current_x][current_y] == 0:
            tomato[current_x][current_y] = 1
            dis[current_x][current_y] += dis[current[0]][current[1]]+1
            Q.append((current_x,current_y))

# 안 익은 토마토가 있는지 확인 flag = 1 이면 모두 익은것이고 , flag = 0 이면 모두 익지 않은 것
flag = 1  
for i in range(m):
    for j in range(n):
        if tomato[i][j] == 0:
            flag = 0

result = 0

# 토마토가 모두 익을 때까지의 최소 일 수 를 찾기 위해 dis 의 최대값을 찾는 것
if flag == 1:
    for i in range(m):
        for j in range(n):
            if dis[i][j] > result:
                result = dis[i][j]
    print(result)
else:
    print(-1)
    