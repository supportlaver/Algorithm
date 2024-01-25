from typing import Optional , List
import collections
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i , cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                stack[last] = i - last
            stack.append(i)
        return res

if __name__ == "__main__":
    s = "bcabc" 
    sol = Solution()
    print(sol.removeDuplicateLetters(s))