
# K : K 개의 정수가 1개씩 주어진다.

k = int(input())
stack = []
for _ in range(k):
    t = int(input())
    if t == 0:
        stack.pop()
    else:
        stack.append(t)

print(sum(stack))

