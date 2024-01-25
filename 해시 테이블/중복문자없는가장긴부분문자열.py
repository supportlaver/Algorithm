
# input = "abcabcbb"
# output = 3


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for char , index in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length , index - start + 1)
            
            used[char] = index
        




            
if __name__ == "__main__":
    input = "abcabcbb"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(input))
        