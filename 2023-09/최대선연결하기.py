n = int(input())
l_nums = [i for i in range(1,n+1)]
l_nums.insert(0,0)
r_nums = list(map(int,input().split()))
r_nums.insert(0,0)

check = [0] * (n+1)
dp = [0] * (n+1)

init = 0
for i in range(1,n+1):
    if l_nums[1] == r_nums[i]:
        init = i

check[1] = init
dp[1] = 1

for i in range(2,n+1):
    cur = 0
    for j in range(1,n+1):
        if l_nums[i] == r_nums[j]:
            cur = j
    for k in range(i-1,0,-1):
        if check[k] > cur:
            break
        else:
            
    dp[i] = 1














