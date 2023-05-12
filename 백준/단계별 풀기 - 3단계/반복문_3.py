price = int(input())
t = int(input())
ssum=0
for _ in range(t):
    a,b=map(int,input().split())
    ssum=ssum+(a*b)

if (ssum==price):
    print("Yes")
else:
    print("No")