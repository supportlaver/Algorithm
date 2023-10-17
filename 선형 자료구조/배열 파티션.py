from typing import List


# 어차피 가장 큰 수를 출력을 해야하기 떄문에
# 최대한 많은 Pair 를 이용하는게 유리할 것

# 오름차순 사용
def arrayPairSum(nums : List[int])->int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum+=min(pair)
            pair = []
    return sum

# 오름차순을 사용해서 구하는 알고리즘은 결국 짝수 인덱스의 num 을 sum 에 더해가고 있다.
# 즉 짝수번째에 있는 수들만 더해가면 그것이 바로 답이 된다.
def arrayPairSum_2(nums : List[int])->int:
    sum = 0
    nums.sort()

    for i in range(len(nums)-1):
        if i%2==0:
            sum+=nums[i]
    return sum

# _2 에 알고리즘을 파이썬 답게 풀면 슬라이싱을 이용하면 된다. (성능도 이게 제일 좋다)
def arrayPairSum_3(nums : List[int])->int:
    return sum(sorted(nums)[::2])

if __name__ == "__main__":
    nums = list(map(int,input().split()))
    print(arrayPairSum_3(nums))