nums = list(map(int,input().split()))
target = int(input())

res = []
# 첫 번째 방법 (브루트 포스) -> 많이 느리다.
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)-1):
        if target == nums[i]+nums[j]:
            res.append(i)
            res.append(j)
print(res)

# 두 번째 방법 (in 탐색)
sed_res = []
for i,n in enumerate(nums):
    complement = target-n
    if complement in nums[i+1:]:
        sed_res.append(nums.index(n))
        sed_res.append(nums[i+1:].index(complement) + (i+1))

print(sed_res)
         
# 세 번째 방법 (첫 번째 수를 뺸 결과 키 조회)
thd_res=[]
nums_map = {}

# 키와 값을 바꿔서 딕셔너리로 저장
for i,num in enumerate(nums):
    nums_map[num] = i

for i,num in enumerate(nums):
    if target-num in nums_map and i!=nums_map[target-num]:
        thd_res.append(i)
        # thd_res.append(nums_map[target-num])
print(thd_res)

