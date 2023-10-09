# 주어지는 문자열 : babad
# 출력 : bab
def longestPalindrome(s):
    def expand(left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    
    # 해당 사항이 없을 경우 빠르게 리턴 해주기 위한 코드
    if len(s)<2 or s==s[::-1]:
        return s
    
    result = ''
    for i in range(len(s)-1):
        result = max(result , expand(i,i+1),expand(i,i+2),key=len)    
    return result

if __name__ == "__main__":
    word = input()
    res = longestPalindrome(word)
    print(res)