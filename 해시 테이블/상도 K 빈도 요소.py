from typing import List
import collections 
import heapq

# input : 1,1,1,2,2,3 , k = 2
# output : 1,2

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqs = collections.Counter(nums)
        freqs_heap = []

        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap , (-freqs[f] , f))
        
        topk = list()
        
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
        return topk
    def topKFrequent_python(self, nums: List[int] , k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
            


        

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    sol = Solution()
    print(sol.topKFrequent(nums,2))
            

        


        
        