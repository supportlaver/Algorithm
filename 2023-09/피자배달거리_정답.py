# 피자집의 개수중 m 개만 뽑는 조합
# cb 에 0 1 2 3 이 들어간 경우는 main 에서 pz 에 피자집의 좌표를 tuple 형태로 넣었고,
# cb 의 0 1 2 3 이 바로 cb 의 인덱스 번호가 되는 것
def DFS(L,s):
    global res
    if L==m:
        # 도시의 피자 거리
        sum=0
        for j in range(len(hs)):
            # 집의 좌표
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            for x in cb:
                # 피자집의 좌표
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis,abs(x1-x2)+abs(y1-y2))
            sum+=dis
        if sum<res:
            res=sum
            
    else:
        for i in range(s,len(pz)):
            cb[L] = i
            DFS(L+1,i+1)

if __name__ == "__main__":
    n,m = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    hs = []
    pz = []
    # 조합의 경우를 넣는 리스트
    cb = [0] * m
    res = 2147000000

    # hs , hz 에 좌표를 넣어서 시작
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                hs.append((i,j))
            elif board[i][j] == 2:
                pz.append((i,j))
    DFS(0,0)
    print(res)
