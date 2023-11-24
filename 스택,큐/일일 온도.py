from typing import List

# 매일의 화씨 온도 리스트를 입력받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 되는가?

# input1 : 73 , 74 , 75 , 71 , 69 , 72 , 76 , 73
# output1 : 1 , 1 , 4 , 2 , 1 , 1 , 0 , 0

# 화씨 73도인 첫째 날에서 더 따뜻한 날을 위해서는 하루만 기다리면 된다.
# 바로 다음날인 둘째 날은 화씨 73도 인데, 마찬가지로 더 따뜻한 날을 위해서는 셋째 날까지 하루만 기다리면 된다.
# 셋째 날은 화씨 75도며, 이보다 더 따뜻한 날을 위해서는 4일을 더 기다리려야 한다.
# 일곱쨰 날과 여덟째 날은 더 이상한 따뜻한 날이 없으므로 각각 0 이다.

class Solution:
    def dailyTemperatures_my(self, temperatures: List[int]) -> List[int]:
        count = []
        for i in range(len(temperatures)-1):
            stack = [temperatures[i]]
            cnt = 1
            for j in range(i+1,len(temperatures)):
                if stack[-1] < temperatures[j]:
                    count.append(cnt)
                    break
                elif j>=len(temperatures)-1:
                    count.append(0)
                    break
                else:
                    cnt+=1
        return count
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i , cur in enumerate(temperatures):
            # 현재 온도가 스택 값보다 높다면 정답 처리
            while stack and cur> temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer

    
if __name__ == "__main__":
    solution = Solution()
    temp = [73 , 74 , 75 , 71 , 69 , 72 , 76 , 73]
    print(solution.dailyTemperatures(temp))




