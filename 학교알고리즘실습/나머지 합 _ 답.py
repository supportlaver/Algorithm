import sys
input = sys.stdin.readline

N,M= map(int, input().split())
num = list(map(int, input().split()))
sum = 0
numRemainder = [0] * M

for i in range(N):
  sum += num[i]
  numRemainder[sum % M] += 1

result = numRemainder[0]

# 나머지가 같은 것들 중에서 2개를 뽑아서 조합을 만든다.
for i in numRemainder:
  result += i*(i-1)//2
  
print(result)