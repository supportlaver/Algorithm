h,m = map(int,input().split())
c=int(input())

# 14 30

cal_m = m+c

quot_h = cal_m // 60
remain_h = cal_m % 60

cal_h = h+quot_h

if cal_h >=24:
    print(cal_h-24,remain_h)
else:
    print(cal_h , remain_h)
    