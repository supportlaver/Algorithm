# input1 : ()[]{}
# output1 : true

# input2 : {[]}
# output2 : 
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0

        
if __name__ == "__main__":
    s = "()[]"
    solution = Solution()
    print(solution.isValid(s))
    