# import sys
# sys.stdin = open("input.txt" , "r")

def DFS(L,x,y,sum):
    if L == n:
        return sum
    else:
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1 and ch[i][j]==0:
                    ch[i][j]=1
                    dis = abs(x-i) + abs(y-j)
                    DFS(L+1,x,y,sum+dis)
                    

if __name__=="__main__":
    n,m = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    
    res = 2157000000
    
    # 0 은 빈칸 , 1은 집 , 2는 피자집

    for i in range(n): # 행
        for j in range(n): # 열
            if board[i][j] == 2:
                ch = [[0] * n for _ in range (n)]
                print(DFS(0,i,j,0))
    
    print(res)



    

