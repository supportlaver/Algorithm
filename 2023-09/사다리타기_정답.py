
# 처음에는 위에서 부터 시작을 하려고 했으나 이렇게 하면 너무 비효율적이다.
# 그래서 일단 맨 마지막 행부터 확인하고 목적지(2) 인 좌표를 먼저 찾는다.
# 그런후 그 좌표에서부터 역으로 올라가서 마지막 행에 도착하면 그 행을 출력하면 된다.
# 맨 밑에서부터 올라가서 맨 마지막 이라는 것은 맨 첫번째 행을 의미하고 맨 첫번째 행은 출발지 열번호이다.

import sys
sys.stdin = open("input.txt" , "r")
def DFS(x,y):
    ch[x][y] = 1
    if x == 0:
        print(y)
    else:
        # 왼쪽
        if y-1>=0 and board[x][y-1]==1 and ch[x][y-1]==0:
            DFS(x,y-1)
        # 오른쪽
        elif y+1<10 and board[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x,y+1)
        # 왼쪽 오른쪽 모두 못 가면 위로
        else:
            DFS(x-1,y)

if __name__ == "__main__":
    board = [list(map(int,input().split()))for _ in range(10)]
    ch = [[0] * 10 for _ in range(10)]
    for y in range(10):
        if board[9][y] == 2:
            DFS(9,y)
    
