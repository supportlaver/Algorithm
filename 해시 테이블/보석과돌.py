# J = "aA"
# S = "aAAbbbb"
# 출력 = 3
import collections
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)

        


        
