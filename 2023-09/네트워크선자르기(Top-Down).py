# 현재 코드 처럼 테이블을 이용하기 떄문에 동적 계획법이 되는 것 , 만약 재귀만 사용한다면 그냥 재귀 함수 일 뿐

def DFS(len):
    # Cut Edge
    if dy[len] != 0:
        return dy[len]
    if len == 1 or len == 2:
        return len
    else:
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]

if __name__=="__main__":
    n = int(input())
    dy = [0] * (n+1)
    print(DFS(n))