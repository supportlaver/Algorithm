import collections
class Solution:
    def isValid(self, s: str) -> str:
        counter,stack = collections.Counter(s) , []

        for char in s:
            counter[char] -= 1
            if char in stack:
                continue

            # 뒤에 붙일 문자가 남아 있다면 스택에 제거
            # stack에 값이 들어있고, 
            # 새로 뽑아온 문자가 stack에 들어있는 문자보다 작고, 
            # counter에 stack의 마지막 글자가 더 있으면 stack에서 꺼내준다.
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)
        
        return ''.join(stack)
    
if __name__ == "__main__":
    s = "cbacdcbc"
    solution = Solution()
    print(solution.isValid(s))