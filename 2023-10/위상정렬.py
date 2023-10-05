# 위상정렬에서는 진입차수가 중요하다.
# degree 라는 리스트에 진입차수의 정보를 넣어준다.
# 1 4 이렇게 들어오면 4 에 진입차수를 1 더해주고
# 4 3 이렇게 들어오면 3 에 진입차수를 1 더해준다는 것
# 진입차수가 0 이라는 것은 바로 실행을 해도 된다는 것이다.
# 진입차수가 2 라는 것은 먼저 2개의 일을 하고 실행을 해야 한다는 것

# 먼저 진입차수가 0 인 작업을 Q 에 넣어준다.
# 그런 후 한 개씩 꺼내면서, 그 작업에서 만드는 진입차수를 없애주면 된다.
# 예를 들어 1 의 진입차수가 0 이라서 Q 에서 뺸 후에 1 에서 만드는 진입차수가 4 라면
# 4 의 진입차수에서 1 를 빼주면 된다.
# 이렇게 빼주면서 진입차수가 0 이 되는 작업이 있다면 그것을 또 Q 에 넣어주면서 반복한다.
# Q 가 빌 때 까지 반복을 하면 된다.

from collections import deque

n,m = map(int,input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
degree = [0] * (n+1)
   
dQ = deque()
for i in range(m):
    a,b= map(int,input().split())
    graph[a][b] = 1
    degree[b] += 1

for i in range(1,n+1):
    if degree[i]==0:
        dQ.append(i)

while dQ:
    x = dQ.popleft()
    print(x,end=" ")
    for i in range(1,n+1):
        if graph[x][i]==1:
            degree[i]-=1
            if degree[i]==0:
                dQ.append(i)