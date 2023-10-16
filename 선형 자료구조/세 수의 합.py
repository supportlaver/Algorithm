from typing import List

# 배열을 입력받아 합으로 0 을 만들 수 있는 3개의 엘리먼트를 출력
# 입력 : [-1,0,1,2,-1,4]
# 출력 : [-1,0,1] , [-1,-1,2]

# O(n^2) - 브루트포스
def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        # 중복된 값 제거 하기 위한 스킵 (i , j , k 모두 동일)
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,len(nums)-1):
            if j>i+1 and nums[j] == nums[j-1]:
                continue
            for k in range(j+1,len(nums)):
                if k>j+1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i] , nums[j] , nums[k]]
                    res.append(temp)
    return res

def threeSum_twoPointer(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i in range(len(nums-2)):
        if i>0 and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = len(nums)-1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]

            if sum <0 :
                left+=1
            elif sum > 0:
                right-=1
            else:
                res.append([nums[i] , nums[left] , nums[right]])
                # 중복된 값 제거 하기 위한 스킵
                while left < right and nums[left] == nums[left+1]:
                    left+=1
                while left < right and nums[right] == nums[right-1]:
                    right-=1
            

if __name__ == "__main__":
    nums = list(map(int,input().split()))
    print(threeSum(nums))
