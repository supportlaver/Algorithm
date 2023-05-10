h,m=map(int,input().split())


# 10시 10분

if m>=45:
    print(h,m-45)
else:
    cal_m = (m-45) + 60
    cal_h = h-1
    if cal_h <0:
        print(cal_h+24 , cal_m)
    else:
        print(cal_h,cal_m)