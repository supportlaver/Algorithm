# 수 N 개가 주어지고, 이때 연속된 부분 구간의 합이 M 으로 나누어 떨어지는 구간의 개수를 구하는 프로그램

# 입력
# 4 2
# 1 2 3 1

# 출력 4

def DFS(L,s):
    global cnt
    if L==2:
        if sum(res) % m == 0:
            for r in res:
                print(r,end=" ")
            print()
            cnt+=1
    else:
        for i in range(s,n):
            res[L] = nums[i]
            DFS(L+1,i+1)

if __name__ == "__main__":
    n,m = map(int,input().split())
    nums = list(map(int,input().split()))
    res = [0] * 2
    cnt = 0
    DFS(0,0)
    print(cnt)