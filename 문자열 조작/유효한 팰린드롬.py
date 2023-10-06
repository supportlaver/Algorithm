from collections import deque
# 방법 1 (리스트)
s = input()
strs = []
for c in s:
    if c.isalnum():
        strs.append(c.lower())
# while len(strs)>1:
#     if strs.pop() != strs.pop(0):
#         print("false")
#         exit(1)
# print("true")

# 방법 2 (데크 자료형)
# 방법 1 에서는 리스트를 사용했지만, 방법 2 에서는 데크 자료형을 사용
# strs = deque()

# 방법 3 (슬라이싱)
if strs == strs[::-1]:
    print("true")
else:
    print("false")




        

