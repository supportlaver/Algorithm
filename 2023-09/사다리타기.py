import sys
sys.stdin = open("input.txt" , "r")
def DFS(x,y,i):
    global res
    if board[x][y] == 2:
        res = i
    else:
        # 오른쪽 또는 왼쪽이 있는지 확인을 해야한다.
        flag = 1
        if y+1<10 and board[x][y+1] == 1 and check[x][y+1] == 0:
            flag = 0
            check[x][y+1] = 1
            DFS(x,y+1,i)
            check[x][y+1] = 0
        if y-1>=0 and board[x][y-1] == 1 and check[x][y-1]==0:
            flag = 0
            check[x][y-1] = 1
            DFS(x,y-1,i)
            check[x][y-1] = 0

        if flag == 1:
            if x+1==10:
                return
            if check[x+1][y] == 0:
                check[x+1][y] == 1
                DFS(x+1,y,i)
                check[x+1][y] == 0
if __name__ == "__main__":
    board = [list(map(int,input().split())) for _ in range(10)]
    
    temp = [i for i in range(10)]
    board.insert(0,temp)
    res = 0
    # 일단 내려가고 -> 왼쪽 or 오른쪽 보고 있으면 왼 or 오 로 먼저 가기 -> 만약 없다면 아래로


    # board[y][x]

    for i in range(10):
        check = [[0]* 10 for _ in range(10)]
        if board[1][i] == 1:
            check[1][i] = 1
            DFS(1,i,i)
        else:
            continue
    print(res)
    
            


    


    
